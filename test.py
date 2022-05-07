import numpy as np
import pytesseract
from PIL import Image

filename = '/Users/sainishwanth/Desktop/Coding/AI-OCR/img1.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)