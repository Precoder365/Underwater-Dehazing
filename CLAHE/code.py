from google.colab.patches import cv2_imshow
import os
import cv2
import math
import numpy as np

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()

def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix

def simplest_cb(img, percent):
    assert img.shape[2] == 3
    assert percent > 0 and percent < 100

    half_percent = percent / 200.0

    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)
        flat = np.sort(flat)

        n_cols = flat.shape[0]

        low_val  = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil( n_cols * (1.0 - half_percent))]

        thresholded = apply_threshold(channel, low_val, high_val)
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

directory = "/content/hazy"

files = os.listdir(directory)
filepaths = [os.path.join(directory, i) for i in files]

# Process each image
for i in filepaths:
    img = cv2.imread(i)
    if img is None:
        continue

    out = simplest_cb(img, 1)
    cv2_imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
    cv2_imshow(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))  
