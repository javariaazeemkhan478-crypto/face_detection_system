<div align="center">

# 🎭 Real-Time Face & Eye Detection System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

A lightweight, blazing-fast real-time face and eye detection application built with Python and OpenCV. 
Perfect for computer vision enthusiasts, security applications, and learning Haar Cascades!

[Features](#-features) •
[Installation](#️-installation) •
[Usage](#-usage) •
[Structure](#-project-structure)

</div>

---

## 🚀 About The Project

This project leverages the power of **OpenCV** and its highly optimized Haar Cascade classifiers to detect faces and eyes in real-time using your computer's webcam. It includes robust camera backend detection to ensure it works smoothly across different operating systems and hardware configurations.

## ✨ Features

- **⚡ Real-Time Detection**: Instantly detects faces and eyes with minimal latency.
- **📷 Smart Camera Initialization**: Automatically cycles through video backends (DirectShow, MSMF, Default) to find a working camera on Windows/Linux/Mac.
- **🌚 Low-Light Optimization**: Uses histogram equalization (`cv2.equalizeHist`) to improve detection accuracy in poorly lit environments.
- **📊 Live Status Panel**: Displays the real-time count of detected faces directly on the video feed.
- **🪞 Mirror Mode**: Flips the camera feed for a more natural user experience.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Computer Vision**: OpenCV (`cv2`)
- **Algorithms**: Haar Cascades (`haarcascade_frontalface_default.xml`, `haarcascade_eye.xml`)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/javariaazeemkhan478-crypto/face_detection_system.git
   cd face_detection_system
   ```

2. **Install dependencies**
   Make sure you have Python installed, then run:
   ```bash
   pip install opencv-python
   ```

## 🚀 Usage

Run the main face detector script:
```bash
python face_detector.py
```

- A window will pop up showing your webcam feed.
- Faces will be highlighted with **green boxes**.
- Eyes will be highlighted with **yellow circles**.
- Press **`Q`** at any time to safely exit the application.

*If you are having trouble with your camera, you can run the diagnostic script:*
```bash
python test_camera.py
```

## 📁 Project Structure

```text
📦 face_detection_system
 ┣ 📜 face_detector.py   # Main application script for detection
 ┣ 📜 test_camera.py     # Diagnostic script to test camera backends
 ┗ 📜 README.md          # Project documentation
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/javariaazeemkhan478-crypto/face_detection_system/issues).

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
<div align="center">
  <b>Built with ❤️</b>
</div>
