import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 segmentation model
model = model  # ← Replace with your model path

# Input/output video paths
input_video_path =    # ← Replace with your video
output_video_path = "output_with_diameters.mp4"

# Open video
cap = cv2.VideoCapture(input_video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (w, h))

# Reference: 267 px = 40 cm
scale = 20 / 267.00187265260894

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    output = frame.copy()
    overlay = np.zeros_like(frame, dtype=np.uint8)

    if results.masks is not None:
        for mask in results.masks.data:
            mask_np = (mask.cpu().numpy() * 255).astype(np.uint8)
            mask_resized = cv2.resize(mask_np, (w, h))
            contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if len(contour) >= 5:
                    cv2.drawContours(overlay, [contour], -1, (60, 60, 60), cv2.FILLED)
                    cv2.drawContours(output, [contour], -1, (255, 255, 0), 1)

                    rect = cv2.minAreaRect(contour)
                    (x, y), (width, height), _ = rect
                    diameter_px = min(width, height)
                    diameter_cm = diameter_px * scale

                    label = f"{diameter_cm:.1f} cm"
                    cv2.putText(output, label, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                                1.1, (0, 0, 255), 4, cv2.LINE_AA)


    # Merge overlay with output
    cv2.addWeighted(overlay, 0.4, output, 0.6, 0, output)

    out.write(output)

cap.release()
out.release()
cv2.destroyAllWindows()
blended = cv2.addWeighted(output, 1.0, overlay, 0.4, 0)
print("✅ Video saved:", output_video_path)
