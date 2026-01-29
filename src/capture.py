import cv2 as cv
import os
from dotenv import load_dotenv
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_DIR = os.path.join(SCRIPT_DIR, "..", "data", "frames" )

os.makedirs(SAVE_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"frame_{timestamp}.jpg"
SAVE_PATH = os.path.join(SAVE_DIR, filename)

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
cv.imwrite(SAVE_PATH, frame)
print(f"Frame saved: {filename}")
print(f"Frame saved to {SAVE_PATH}")

# Cleanup
cap.release()
