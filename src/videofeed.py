import cv2
import threading
import queue
import time
import os

#forces TCP 
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

class ThreadedCamera:
    def __init__(self, src):
        self.capture = cv2.VideoCapture(src)
        #queue for frames (max 2 frames)
        self.q = queue.Queue(maxsize=2)
        self.running = True
        
        #thread for updating frames
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.running:
            if not self.capture.isOpened():
                time.sleep(0.1)
                continue
                
            ret, frame = self.capture.read()
            if not ret:
                continue
            
            #waits for queue to be not full
            #removes old frame if queue is full
            if self.q.full():
                try:
                    self.q.get_nowait()
                except queue.Empty:
                    pass
            
            #adds the new frame
            self.q.put(frame)

    def read(self):
        return self.q.get()
    
    def stop(self):
        self.running = False
        self.capture.release()

rtsp_url = "rtsp://localhost:554/live"

print("Starting Threaded Capture...")
cam = ThreadedCamera(rtsp_url)

time.sleep(1)

#creates resizeable window
cv2.namedWindow("Video Feed", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Video Feed", 1280, 720)

while True:
    try:
        #gets the newest frame
        frame = cam.read()
        
        #YOLO code will go here
        
        cv2.imshow("Video Feed", frame)
        
    except queue.Empty:
        pass #no frames ready 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.stop()
cv2.destroyAllWindows()
