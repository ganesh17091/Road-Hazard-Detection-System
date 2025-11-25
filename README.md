# Road-Hazard-Detection-System
Problem Statement: Drivers  cannot  always  detect  nearby  risks  due  to  human  limitations  and  line-of-sight  restrictions.  Without  real-time  awareness  shared  between  vehicles, many preventable road collisions still occur. 

# 🚘 AI-Assisted Driver Awareness System Using V2V Communication

This project implements a **real-time vehicle-to-vehicle (V2V) safety system** using **NVIDIA Jetson devices**, **YOLOv11 object detection**, and **wireless data exchange** over Wi-Fi.  
Each vehicle detects road hazards using onboard AI and **broadcasts simplified hazard information** to nearby vehicles, improving driver awareness and reducing collisions — especially in low-visibility or line-of-sight-blocked situations.

---

## 🚀 Key Features

| Feature | Description |
|--------|-------------|
| On-device YOLOv11 detection | Real-time inference on Jetson without the internet |
| V2V communication | Hazard information shared among nearby vehicles |
| JSON-based protocol | Lightweight and fast for embedded systems |
| Simple driver UI | Alerts displayed in easy-to-understand text |
| GPS-aware communication | Every broadcast includes real-time vehicle location |
| Fully scalable | Works with 2, 10, or 100 vehicles on same network |

---

## 🧠 System Architecture

Camera → YOLOv11 AI → JSON hazard packet → Wi-Fi broadcast (UDP) → Receiver → Risk analysis → Display alert to driver


Each Jetson runs **both modules**:
- One to **broadcast its own detections**
- One to **receive detections from others** and **warn the driver**

---

## 📂 Repository Structure

📁 Road-Hazard-Detection
│
├── v2v_sender.py # YOLO detection + JSON broadcast
├── driver_display.py # Receive data + driver alert display
│
├── models/
│ └── yolo11n.pt # YOLO model 




---

## 📦 Software Requirements

| Component | Version Recommended |
|----------|---------------------|
| JetPack / Ubuntu | 4.6 or later |
| Python | 3.8+ |
| YOLO Framework | ultralytics |
| OpenCV | ≥ 4.2 |
| GPSD (if GPS module attached) | gpsd-py3 |
| Wi-Fi | Any access-point or hotspot mode |

Install dependencies:

```bash
pip install ultralytics opencv-python gpsd-py3
