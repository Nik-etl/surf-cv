import cv2 as cv
import os
from dotenv import load_dotenv

load_dotenv()

source = os.getenv("SOURCE_URL","No URL found")
print(source) #for debugging

cap = cv.VideoCapture(source)

if not cap.isOpened():
    print("ERROR: Could not connect ot RTSP stream")
    exit()

print("Connected to stream")

ret, frame = cap.read()

if not ret:  
    print("ERROR: Connectec but could not read frame")
    cap.release()
    exit()

print(f"Frame captured: {frame.shape}") #Shows dimensions 

# save frame
#TODO turn this into relative file path 
cv.imwrite("../data/frames/capturedframe.jpg", frame)
print("Frame saved as captured_frame.jpg")

# Cleanup
cap.release()
