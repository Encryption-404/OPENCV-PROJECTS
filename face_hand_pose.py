import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic() as holistic: 
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Detections
        results = holistic.process(image)
        #print(results.face_landmarks)
        #drawing the images
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
       # mp_drawing.draw_landmarks(image, results.face_landmarks)
        mp_drawing.draw_landmarks(
                image,              # Image to draw on
               results.face_landmarks, # Connections between face landmarks
               landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 200, 0), thickness=1, circle_radius=1), # Customize dot appearance
               connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1), # Customize connection appearance
)
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()