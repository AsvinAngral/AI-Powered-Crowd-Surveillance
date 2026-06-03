import cv2
from ultralytics import YOLO
from sort.sort import Sort 
import os
import numpy as np


# Load the YOLOv8 model
model = YOLO("yolov8l.pt")

# Initialize SORT tracker
tracker = Sort()

# Path to your input video
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("tracked_output.mp4", fourcc, fps, (width, height))

# Store track history
tracks_history = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO object detection
    results = model(frame)[0]

    # Extract person class detections only
    detections = []
    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box
        if int(cls) == 0:  # class 0 is 'person'
            detections.append([x1.item(), y1.item(), x2.item(), y2.item(), conf.item()])
    
    # Convert to NumPy array
    detections = np.array(detections)
    
    # Update tracker with detections
    tracks = tracker.update(detections)

    # Track current frame's people IDs
    track_ids = []

    for track in tracks:
        x1, y1, x2, y2, track_id = track
        x1, y1, x2, y2, track_id = int(x1), int(y1), int(x2), int(y2), int(track_id)

        track_ids.append(track_id)

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Track center point for path
        center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
        if track_id not in tracks_history:
            tracks_history[track_id] = []
        tracks_history[track_id].append(center)

        # Draw path history
        for j in range(1, len(tracks_history[track_id])):
            cv2.line(frame, tracks_history[track_id][j - 1], tracks_history[track_id][j], (0, 0, 255), 2)

    # Show people count at top
    cv2.putText(frame, f'People Count: {len(track_ids)}', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Write frame to output video
    out.write(frame)

    # Show live window
    cv2.imshow("Crowd Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
