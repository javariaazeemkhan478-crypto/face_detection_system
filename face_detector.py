import cv2
import os

print("Loading detector... please wait")

# Load OpenCV's built-in face + eye detectors (no extra libraries needed!)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

print("Detector ready! Trying to open camera...")

# Auto-detect working camera backend
cap = None
for backend, name in [(cv2.CAP_DSHOW, "DirectShow"),
                      (cv2.CAP_MSMF, "MSMF"),
                      (0, "Default")]:
    test = cv2.VideoCapture(0, backend)
    if test.isOpened():
        ret, frame = test.read()
        if ret and frame is not None:
            cap = test
            print(f"✅ Camera working with {name}!")
            break
        test.release()

if cap is None:
    print("❌ Camera not found! Check privacy settings.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("✅ Camera opened! Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    # Flip like a mirror
    frame = cv2.flip(frame, 1)

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)  # improves detection in low light

    # ── Detect Faces ──
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    # ── Draw Face Boxes ──
    for (x, y, w, h) in faces:
        # Green box for face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # ── Detect Eyes inside each face ──
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
        for (ex, ey, ew, eh) in eyes:
            cv2.circle(roi_color,
                      (ex + ew // 2, ey + eh // 2),
                      ew // 2, (255, 255, 0), 2)  # Yellow circles for eyes

    # ── Status Panel ──
    cv2.rectangle(frame, (0, 0), (210, 70), (0, 0, 0), -1)
    cv2.putText(frame, f"Faces : {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, "Q = Quit", (10, 58),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow("Face + Eye Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Closed successfully!")