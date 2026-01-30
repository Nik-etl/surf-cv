import cv2 as cv
import os
from dotenv import load_dotenv
from datetime import datetime
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_DIR = os.path.join(SCRIPT_DIR, "..", "data", "frames" )

os.makedirs(SAVE_DIR, exist_ok=True)

load_dotenv()

source = os.getenv("SOURCE_URL","No URL found")
print(source) #for debugging

cap = cv.VideoCapture(source)

if not cap.isOpened():
    print("ERROR: Could not connect ot RTSP stream")
    exit()

print("Connected to stream")

frames = 0 

while frames < 5:
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"frame_{timestamp}.jpg"
    SAVE_PATH = os.path.join(SAVE_DIR, filename)
    
    ret, frame = cap.read()

    if not ret:  
        print("ERROR: Connected but could not read frame")
        cap.release()
        exit()
    
    print(f"Frame captured: {frame.shape}") #Shows dimensions 

    cv.imwrite(SAVE_PATH, frame)
    print(f"Frame saved: {filename}")
    print(f"Frame saved to {SAVE_PATH}")
    time.sleep(10)
    frames += 1

# Cleanup
cap.release()
