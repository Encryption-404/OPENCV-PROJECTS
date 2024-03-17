import cv2
import mediapipe as mp
import numpy as np


cap = cv2.VideoCapture(0)
mp_draw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh=mpFaceMesh.FaceMesh(max_num_faces=1)

# Define the connections between landmarks manually
connections = [
    (10, 338), (338, 297), (297, 332), (332, 284), (284, 251), (251, 389), (389, 356), (356, 454),
    (454, 323), (323, 361), (361, 288), (288, 397), (397, 365), (365, 379), (379, 378), (378, 400),
    (400, 377), (377, 152), (152, 148), (148, 176), (176, 149), (149, 150), (150, 136), (136, 172),
    (172, 58), (58, 132), (132, 93), (93, 234), (234, 127), (127, 162), (162, 21), (21, 54), (54, 103),
    (103, 67), (67, 109), (109, 10)
]

while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            cv2.putText(img,str("FACE DETECTED"),(300,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
            for faceLms in results.multi_face_landmarks:  
                # Draw landmarks with custom parameters including connections
                #mp_draw.draw_landmarks(
                  #  img,
                  #  faceLms,
                  #  connections,  # Manual specification of connections
                  #  landmark_drawing_spec=mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),  # Customize dot appearance
                  #  connection_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1),  # Customize connection appearance
              #  )
                   # Extract landmark coordinates
                landmark_coords = [(lm.x, lm.y) for lm in faceLms.landmark]
            
            # Calculate bounding box coordinates
                xmin = int(min(landmark_coords, key=lambda x: x[0])[0] * img.shape[1])
                xmax = int(max(landmark_coords, key=lambda x: x[0])[0] * img.shape[1])
                ymin = int(min(landmark_coords, key=lambda x: x[1])[1] * img.shape[0])
                ymax = int(max(landmark_coords, key=lambda x: x[1])[1] * img.shape[0])
            
            # Draw a square around the face
                cv2.rectangle(img, (xmin-20, ymin-10), (xmax+20, ymax+20), (0, 0, 200), 1)
        
        
        cv2.imshow('FACE Tracking', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
