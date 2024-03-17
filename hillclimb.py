import numpy as np
import mediapipe as mp
import cv2
import time
import math
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
currenttime=0
prevtime=0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.4,
    min_tracking_confidence=0.4,
    max_num_hands=1) as hands:

    while cap.isOpened():

        success, image = cap.read()
        
        h, w, c = image.shape

       

        # Flip the image horizontally for a later selfie-view display
        # Convert the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Process the image and find hands
        results = hands.process(image)

     
        # Draw the hand annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
     
        if results.multi_hand_landmarks:
            right_hand_landmarks = results.multi_hand_landmarks[0]

            mp_drawing.draw_landmarks(
                image, right_hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2),
            mp_drawing_styles.DrawingSpec(color=(0,244,0), thickness=2, circle_radius=2))
            
            
           
            cv2.putText(image,"MOVE LEFT OR RIGHT", (200,70), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,200,0), 2)
            index_finger_tip =right_hand_landmarks.landmark[12]
            center = right_hand_landmarks.landmark[0]
            index_finger_tip_x = index_finger_tip.x * w
            index_finger_tip_y = index_finger_tip.y * h
            center_x = center.x * w
            center_y = center.y * h
            length=math.hypot(center_x-index_finger_tip_x ,center_y-index_finger_tip_y)
            print(length)
            if(length<70):
                pyautogui.keyUp('right')
                pyautogui.keyUp('left')
            if index_finger_tip_x > w*0.7:
                cv2.putText(image,"GAS", (500,70), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)
                pyautogui.keyDown('right')
                pyautogui.keyUp('left')
            elif index_finger_tip_x < w*0.3:
                cv2.putText(image,"BRAKE", (500,70), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,0), 2)
                pyautogui.keyDown('left')
                pyautogui.keyUp('right')
           

        cv2.line(image, (int(w*0.3), 0), (int(w*0.3), h), (255,0, 0), 1)
        cv2.line(image, (int(w/2), 0), (int(w/2), h), (255, 0, 0), 1)
        cv2.line(image, (int(w*0.7), 0), (int(w*0.7), h), (255,0, 0), 1)

        currenttime=time.time()
        fps=1/(currenttime-prevtime)
        prevtime=currenttime    
        cv2.putText(image,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

            
        cv2.imshow('MediaPipe Hands', image)



        if cv2.waitKey(5) & 0xFF == 27:
          break

cap.release()