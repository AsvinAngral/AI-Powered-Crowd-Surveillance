
# Real-Time Crowd Detection and Tracking System

### 🎓 Accepted in Springer (Scopus Indexed) | Built using YOLOv8 + SORT | Research + Real-time Application

## 📌 Overview

This project implements a real-time **Crowd Detection and Tracking System** using the **YOLOv8 object detection model** and the **SORT tracking algorithm**. It is capable of identifying individuals in crowded scenes, assigning unique IDs, tracking their movement paths, and displaying a real-time crowd count per frame. The system outputs a processed video with annotated bounding boxes, IDs, and motion trajectories.

This solution was developed as part of an academic research project and has been **peer-reviewed and accepted for publication in a Springer Scopus-indexed journal**.

## Certification -
<img width="550" height="480" alt="image" src="https://github.com/user-attachments/assets/5f7831b9-76fa-48f4-b251-2d0be3123d93" />


## ▶️ Output Video -



[https://github.com/user-attachments/assets/770698ba-6ff8-4495-b709-128080a5c0e9](https://www.youtube.com/watch?v=--dhq1QuDEk)

## 📷 Screenshot -
![image](https://github.com/user-attachments/assets/335f7b6d-a03d-4b3a-8fb5-af0f740a9a80)
![image](https://github.com/user-attachments/assets/881ad16c-3ca2-4101-97cb-d4ab8b91bbf3)

## 🧠 Key Features

- 👁️‍🗨️ Real-time object detection with **YOLOv8**
- 🧭 Multi-object tracking with **SORT (Kalman Filter + Hungarian Matching)**
- 📈 Dynamic people count overlay per frame
- 🔴 Visual trail drawing for individual motion paths
- 📹 Video input/output support with OpenCV
- 💻 Modular and GPU-accelerated (runs on both CPU and GPU)
- 📄 Based on research-backed methodology with real-world validations

## 📁 Project Structure

```
├── crowd_tracker.py             # Main application script
├── sort/                        # SORT tracking implementation
├── yolov8l.pt                   # YOLOv8 large model weights (downloaded via Ultralytics)
├── tracked_output.mp4          # Output video with annotations
├── video.mp4                   # Input test video
├── README.md                   # Project documentation
```

## 🚀 How It Works

1. **YOLOv8** detects people in each frame (class 0 of COCO dataset).
2. Bounding boxes with confidence scores are passed to **SORT**.
3. SORT assigns a unique ID to each detected person and tracks their movement.
4. Paths are visualized using line trails.
5. Frame-wise people count is displayed on the top of the video.
6. Output is saved as an annotated video (`tracked_output.mp4`).

## 🛠️ Requirements

- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV (`opencv-python`)
- NumPy
- SORT implementation (`filterpy`, `skimage`) 

Make sure your input video (`video.mp4`) is in the same directory. The output will be saved as `tracked_output.mp4`. To quit live display, press `q`.

## 📊 Dataset Used

- **ShanghaiTech Crowd Counting Dataset** (used during evaluation and benchmarking)
- Real-time CCTV-like footage for testing edge cases (occlusion, motion blur, night view)

## 📑 Research Publication

This project was supported by in-depth research and experimentation and has been **accepted in a Springer Scopus-indexed international journal**. The research focused on:

- Model accuracy in dense environments
- Performance across lighting conditions
- Real-time tracking under resource constraints
- Ethical considerations in crowd monitoring

_Acceptance proof_

## ⚠️ Ethical Note

This system **does not store personal or facial data**, ensuring compliance with privacy regulations such as **GDPR**. It is designed strictly for research, academic, and public safety purposes.

## 💡 Future Improvements

- Integrate Deep SORT or ByteTrack for stronger tracking performance
- Add heatmap visualization and statistical reports
- Enable cloud/edge deployment for large-scale CCTV infrastructure
- Develop a full web dashboard for remote monitoring

## 👨‍💻 Author

**Abhay Jasrotia**  
B.Tech Computer Science – Chandigarh University.  
Researcher | AI/ML | Softerware Tester | QA Automation   
