import cv2
import numpy as np

# --- Load video file ---
video_path = r"C:\Users\padma\OneDrive\motion detection project\factory video.mp4"
video = cv2.VideoCapture(video_path)

# --- Check if video opened successfully ---
if not video.isOpened():
    print(f"Error: Could not open video file at {video_path}")
    exit()

# --- Read first two frames ---
ret, frame1 = video.read()
ret, frame2 = video.read()

# --- Motion detection parameters ---
MIN_CONTOUR_AREA = 1000      # Ignore small noise
THRESHOLD_SENSITIVITY = 25   # Higher value = less sensitive
BLUR_SIZE = (7, 7)

print("Running motion detection... Press ESC to quit.")

while video.isOpened():
    # Compute difference between frames
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, BLUR_SIZE, 0)

    # Threshold the difference
    _, thresh = cv2.threshold(blur, THRESHOLD_SENSITIVITY, 255, cv2.THRESH_BINARY)

    # Dilate to fill in holes and reduce flicker
    dilated = cv2.dilate(thresh, None, iterations=3)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    # Find contours of moving objects
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < MIN_CONTOUR_AREA:
            continue
        motion_detected = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display text if motion detected
    if motion_detected:
        cv2.putText(frame1, "MOTION DETECTED", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show result in popup window
    cv2.imshow("Factory Motion Detection", frame1)

    # Prepare next frame
    frame1 = frame2
    ret, frame2 = video.read()
    if not ret:
        print("Video ended.")
        break

    # Press ESC to quit early
    if cv2.waitKey(30) == 27:
        break

# --- Cleanup ---
video.release()
cv2.destroyAllWindows()
print("Motion detection finished.")
