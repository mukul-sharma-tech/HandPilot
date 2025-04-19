🖐️ Hand Gesture Virtual Mouse with 3D Overlay
This project uses computer vision and hand gesture recognition to control the mouse cursor and simulate mouse events such as left click, right click, double click, and scrolling using hand gestures. It also includes a 3D overlay visualization of the hand using MediaPipe.

📽️ Demo
<img src="https://www.linkedin.com/posts/mukul-sharma-830a152b2_ai-computervision-gesturecontrol-activity-7309922207214825473-Kyys?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEtBz2QBZ3-aq9VHReVvW2227J9ZyVQgHuQ" alt="Live Demo">
A webcam video feed is used to track hand landmarks in real time. Your index finger controls the mouse cursor, and gestures control mouse actions.

🧠 Features
🖱️ Move mouse with index finger tip

👆 Left-click using Index + Thumb

👉 Right-click using Index + Middle Finger

🔃 Scroll using Middle finger above/below index

🧠 3D Hand overlay showing depth with dynamic radius and color

💻 Real-time performance using MediaPipe Hands

🧰 Tech Stack
Python

OpenCV (cv2)

MediaPipe (Google’s ML framework for hands detection)

PyAutoGUI (for mouse control)

NumPy

🖥️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/mukul-sharma-tech/HandPilot.git
cd HandPilot
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui numpy

Run the script
python HandPilot.py

📌 Usage Instructions
Make sure your webcam is turned on.
Use your index finger to move the cursor.
Pinch index finger and thumb to left-click.
Bring index and middle finger tips close together to right-click.
Move middle finger up/down relative to index to scroll.
Press q to quit.


🧠 Gesture Logic Summary
Gesture	Action
Index Finger	Move Cursor
Index + Thumb (pinch)	Left Click
Index + Thumb (pinch x2)	Double Click
Index + Middle (pinch)	Right Click
Middle above/below Index	Scroll Up/Down
🎨 3D Hand Overlay
Each joint is shown as a circle with size and color based on depth (z-axis).

Connections are shown with dynamic thickness depending on depth.

🛠️ Customize
You can tweak:

Click distances (< 30, < 25)

Scroll threshold (> 20)

Overlay radius and color mapping

🤝 Contributing
Pull requests are welcome! If you find bugs or have improvements in mind (like gesture customization, streamlit integration, or web version), feel free to contribute.
