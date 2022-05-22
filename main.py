import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
from pyfirmata import Arduino, SERVO, util
import time
import os
from playsound import playsound
from gtts import gTTS

# pyfirmata stuff
port = 'COM3'
pin = 2
board = Arduino(port)

board.digital[pin].mode = SERVO

board.digital[pin].write(50)

it = util.Iterator(board)
it.start()

while True:
    time.sleep(0.1)

    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic

    opened = False


    cap = cv2.VideoCapture(1)
    # Initiate holistic model
    #=======
    frames = 0
    #=======

    memory = {
        "last_frame_washed": 0,
        "frames_washed": 0,
        "clean": False
    }



    def find_overlap(lhpts, rhpts):
        overlap_xy = 0
        for lhpt in lhpts:
            if lhpt[0] < mostright_rhpt_x:
                if lhpt[1] > lowest_rhpt_y and lhpt[1] < highest_rhpt_y:
                    overlap_xy += 1
                    
        return overlap_xy

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
        while cap.isOpened():
            if opened:
                board.digital[pin].write(140)  
            else:
                board.digital[pin].write(50)


            #=======
            frames += 1
            if memory["last_frame_washed"] - frames >= 25 * 15: # 25 frames times 30 seconds
                memory["frames_washed"] = 0
                memory["clean"] = False

            print()
            if memory["clean"] == False:
                if memory["frames_washed"] >= 30:
                    print("You are clean!")
                    memory["clean"] = True
                    opened = True
                    clean_audio_file = gTTS("You are clean and cleared!")
                    clean_audio_file.save("clean.mp3")
                    playsound("clean.mp3")
                elif memory["frames_washed"] < 100 and memory["frames_washed"] >= 1:
                    print("Keep washing! You have washed for " + str(memory["frames_washed"]) + "frames.")
            #=======
            ret, frame = cap.read()
            
            # Recolor Feed
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Make Detections
            results = holistic.process(image)

            if results.right_hand_landmarks != None and results.left_hand_landmarks != None:
                allpts = []
                ex = []
                why = []
                print("===========")
                
                rhpts = []
                rhpts_x = []
                rhpts_y = []
                for i in results.right_hand_landmarks.landmark:
                    x = int(i.x*cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    y = int((1 - i.y)*cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    rhpts_x.append(x)
                    rhpts_y.append(y)
                    rhpts.append((x,y))
                mostleft_rhpt_x = min(rhpts_x)
                mostright_rhpt_x = max(rhpts_x)
                lowest_rhpt_y = min(rhpts_y)
                highest_rhpt_y = max(rhpts_y)

                lhpts = []
                lhpts_x = []
                lhpts_y = []
                for i in results.left_hand_landmarks.landmark:
                    x = int(i.x*cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    y = int((1 - i.y)*cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    lhpts_x.append(x)
                    lhpts_y.append(y)
                    lhpts.append((x,y))
                mostleft_lhpt_x = min(lhpts_x)
                mostright_lhpt_x = max(lhpts_x)
                lowest_lhpt_y = min(lhpts_y)
                highest_lhpt_y = max(lhpts_y)

                if mostleft_lhpt_x - mostright_rhpt_x < 30:
                    memory["frames_washed"] += 1
                    memory["last_frame_washed"] = frames

            # Recolor image back to BGR for rendering
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Right hand
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Left Hand
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            cv2.imshow('Raw Webcam Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()