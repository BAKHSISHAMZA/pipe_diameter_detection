"""
# Pipe Diameter Detection with YOLOv8 Segmentation

This project aims to detect pipes in images/videos and estimate their real-world diameters using YOLOv8 segmentation.

## Features
- Pipe segmentation using YOLOv8
- Diameter estimation in cm using a reference object
- Supports images and videos
- Visual output with overlays of contours and diameter values

## Project Phases
1. Dataset Collection & Manual Annotation (Roboflow)
2. Training YOLOv8 Segmentation Model
3. Manual calibration using known pipe diameter (40 cm)
4. Real-world diameter computation
5. Visualization with OpenCV

## Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run on an image
python inference/image_inference.py --img_path images/sample_image.jpg

# Run on a video
python inference/video_inference.py --video_path videos/input_video.mp4
```

## Credits
Created by HAMZA BAKHSIS.
"""
