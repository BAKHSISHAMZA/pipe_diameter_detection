# Stores your 267 pixel = 40 cm conversion logic
REF_DIAMETER_CM = 40
REF_DIAMETER_PX = 267.0

def pixels_to_cm(px):
    return (px / REF_DIAMETER_PX) * REF_DIAMETER_CM
