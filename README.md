This project detects motion in a factory video using the Frame Differencing technique implemented with OpenCV in Python. It analyzes consecutive frames from a video, identifies regions where pixel intensity changes significantly, and highlights those areas with green bounding boxes.

This method is useful for industrial surveillance, automation monitoring, and safety alert systems.

🎯 Objective

To create a computer vision system that can detect and highlight motion in a video feed using frame differencing and contour detection techniques.

🧠 How It Works

The program reads two consecutive frames from the video.

It calculates the absolute difference between them.

The difference is converted to grayscale and blurred to remove noise.

Thresholding and dilation are applied to emphasize motion regions.

Contours are drawn around detected moving objects.

When motion is detected, the text “MOTION DETECTED” appears on the screen.

🧩 Files Included
motion detection project/
│
├── main.py                # Main Python code for motion detection
├── factory video.mp4      # Sample video file (place your own video here)
└── README.txt              # Project documentation

⚙️ Requirements

Python 3.10+

OpenCV library

Install OpenCV with:

pip install opencv-python

▶️ How to Run

Place your video (e.g., factory video.mp4) in the same folder as main.py.

Open VS Code terminal or Command Prompt in that folder.

Run the program:

python main.py


A window will pop up showing your video.

Moving objects will be highlighted with green boxes.

“MOTION DETECTED” will appear on active movement.

Press ESC to exit.
