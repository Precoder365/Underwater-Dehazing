Haze Removal:

For each color channel
- The pixel intensities are flattened into a 1-dimensional array and sorted.
- Low and high threshold values are calculated based on a specified percentage of pixels.
- Thresholding is applied to the channel, where pixel intensities below the low threshold are set to the threshold value and intensities above the high threshold are set to the high threshold value.
- The pixel intensities are normalized using cv2.normalize.
- The processed color channels are merged back together into a single image using cv2.merge.
