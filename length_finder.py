import cv2
import mediapipe as mp
import time
import math
import pyautogui
cap=cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

currenttime=0
prevtime=0

   
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results =hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
          for id,lm in enumerate(handLms.landmark):
#------------------------------------------------------------------------------------------------------------------------------------------------------
            #  print(id,lm)
            h, w, c=img.shape
             
                
            
            
          
            if id ==4:
               x1,y1=int(lm.x*w),int(lm.y*h)
               cv2.circle(img,(x1,y1),1,(0,255,0),cv2.FILLED)
            if id ==8:
               x2,y2=int(lm.x*w),int(lm.y*h)
               cv2.circle(img,(x2,y2),1,(0,255,0),cv2.FILLED)
            
               cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
               length=math.hypot(x2-x1,y2-y1)
               if length<21:
                 length=0
                 print(length) 
                 cv2.putText(img,str(int(length)),(300,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
               else:
                 print(length) 
                 cv2.putText(img,str(int(length)),(300,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
          
          
          
          
          
          
#------------------------------------------------------------------------------------------------------------------------------------------------- 
          mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)  
            
    currenttime=time.time()
    fps=1/(currenttime-prevtime)
    prevtime=currenttime    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
    cv2.imshow('Hand Tracking', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()