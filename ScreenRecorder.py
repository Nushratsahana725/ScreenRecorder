import cv2
import numpy as np
import pyautogui


screen_size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"MPEG")
out=cv2.VideoWriter("output.mp4",fourcc,20.0,(screen_size))


while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("SS recorder by Manoj",frame)
    if cv2.waitKey(1)==ord("q"):
        break
