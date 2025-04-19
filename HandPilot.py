import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Open webcam
cap = cv2.VideoCapture(0)

# Track last click time for double-click detection
last_click_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmark positions
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Convert to pixel coords
            x, y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)

            # Map to screen size
            screen_x = np.interp(x, [0, w], [0, screen_width])
            screen_y = np.interp(y, [0, h], [0, screen_height])
            pyautogui.moveTo(screen_x, screen_y, duration=0.1)

            # === Left Click Gesture (Thumb + Index) ===
            dist_thumb_index = np.hypot(thumb_x - x, thumb_y - y)
            if dist_thumb_index < 30:
                current_time = time.time()
                if current_time - last_click_time < 0.3:
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time
                pyautogui.sleep(0.2)

            # === Right Click Gesture (Index + Middle) ===
            dist_index_middle = np.hypot(middle_x - x, middle_y - y)
            if dist_index_middle < 25:
                pyautogui.rightClick()
                pyautogui.sleep(0.3)

            # === Scroll Gesture (Middle finger relative to Index) ===
            scroll_distance = middle_y - y
            if abs(scroll_distance) > 20:
                pyautogui.scroll(-5 if scroll_distance > 0 else 5)

            # --- 3D Virtual Hand Overlay ---
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                depth = lm.z
                radius = int(np.interp(depth, [-0.2, 0.1], [15, 5]))
                color = int(np.interp(depth, [-0.2, 0.1], [255, 50]))
                cv2.circle(frame, (cx, cy), radius, (color, 255 - color, 150), -1)

            for connection in mp_hands.HAND_CONNECTIONS:
                start = hand_landmarks.landmark[connection[0]]
                end = hand_landmarks.landmark[connection[1]]
                x1, y1 = int(start.x * w), int(start.y * h)
                x2, y2 = int(end.x * w), int(end.y * h)
                thickness = int(np.interp((start.z + end.z) / 2, [-0.2, 0.1], [5, 1]))
                cv2.line(frame, (x1, y1), (x2, y2), (200, 200, 250), thickness)

    cv2.imshow("Hand Cursor Control (3D Overlay)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
