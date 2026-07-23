import cv2

for index in [0, 1, 2]:
    for backend, name in [(cv2.CAP_DSHOW, "DirectShow"), (cv2.CAP_MSMF, "MSMF"), (0, "Default")]:
        cap = cv2.VideoCapture(index, backend)
        if cap.isOpened():
            ret, frame = cap.read()
            print(f"✅ Camera {index} with {name} WORKS! ret={ret}")
            cap.release()
        else:
            print(f"❌ Camera {index} with {name} failed")