"""
Simple photo preparation for ASCII conversion (no AI background removal).
Boosts contrast and saves as grayscale. Works on Windows without rembg/onnxruntime.

Usage: python scripts/prep_photo_simple.py [input.jpg] [output.png]
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

# 1. Load image as grayscale
img = cv2.imread(INP, cv2.IMREAD_COLOR)
if img is None:
    print(f"Error: could not load {INP}")
    sys.exit(1)

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Apply CLAHE (local contrast enhancement)
clahe = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8))
gray = clahe.apply(gray)

# 4. Slight global brightness/contrast lift
gray = cv2.convertScaleAbs(gray, alpha=1.05, beta=18)

# 5. Save as grayscale PNG
Image.fromarray(gray, mode="L").save(OUT)
print(f"wrote {OUT}  {gray.shape}")
