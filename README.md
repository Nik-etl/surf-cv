# surf-cv

Coastal monitoring system using computer vision to analyze surf conditions from live camera feeds.

## Project Goals
- Capture frames from live surf cam streams
- Count surfers/ people in water
- Classify water conditions (planned)
- Store historical data for trend analysis (planned)

## Status
Work in progress - frame capture pipeline functional. Detects persons in frame using YOLOv8s. 
*Currently fine tuning model*

## Tech Stack
- Python
- OpenCV
- ultralytics yolov8
- Raspberry Pi 5 (deployment target)

## Setup
1. Clone repo
2. Create virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with `SOURCE_URL=your_stream_url`
5. Run: `python src/capture.py`
