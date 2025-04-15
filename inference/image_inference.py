import cv2
import numpy as np
from ultralytics import YOLO

# Load model
model =   # Replace with your model path

# Load image
image_path =   # Replace with your image path
image = cv2.imread(image_path)
image = cv2.resize(image,(1080,720))

# Inference
results = model(image)[0]

# Reference: 267 pixels = 40 cm → scale = cm/pixel
scale = 40 / 267.00187265260894

# Prepare image for drawing
output = image.copy()

# Iterate over masks
for mask in results.masks.data:
    # Convert mask to numpy format
    mask_np = mask.cpu().numpy().astype(np.uint8) * 255

    # Find contours
    contours, _ = cv2.findContours(mask_np, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Get bounding ellipse if possible
        if len(contour) >= 5:  # fitEllipse needs at least 5 points
            ellipse = cv2.fitEllipse(contour)
            (x, y), (MA, ma), angle = ellipse  # MA: major axis, ma: minor axis

            # Estimate diameter as average of major and minor axes
            diameter_px = (MA + ma) / 2
            diameter_cm = diameter_px * scale

            # Draw contour and ellipse
            cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)
            cv2.ellipse(output, ellipse, (0, 0, 255), 2)

            # Put text
            text = f"{diameter_cm:.1f} cm"
            cv2.putText(output, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Save or display result
cv2.imwrite("output_with_diameters.jpg", output)
cv2.imshow("Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

