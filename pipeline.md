1. **Color Correction**:
    - **Purpose**: Underwater scenes often suffer from color distortion due to the absorption and scattering of light. Color correction helps restore accurate color representation, compensating for the loss of certain wavelengths of light underwater.
    - **Actions**:
        - Adjusts color balance to counteract the dominant blue or green hues often present in underwater images.
        - Compensates for color attenuation caused by the absorption of light at different depths, ensuring a more natural and vibrant appearance.

2. **Total Variation Denoising**:
    - **Purpose**: Underwater images may contain noise introduced by factors such as low light conditions, water particles, or camera sensors. Denoising helps improve the clarity and visibility of objects in the image by reducing this noise.
    - **Actions**:
        - Applies total variation denoising to smooth out variations in pixel intensity while preserving important features in the underwater scene, such as coral reefs, marine life, or structures.

3. **Guided Filter**:
    - **Purpose**: In underwater environments, preserving fine details such as the textures of marine life or the outlines of objects is crucial for maintaining image quality. The guided filter helps achieve this by smoothing noise while preserving edges and textures.
    - **Actions**:
        - Utilizes the guided filter to enhance the denoising process while preserving important image structures, resulting in clearer and more visually appealing underwater images.
      1. **Initialization**:
         - The guided filter requires two input images: the guidance image \(I\) and the target image \(P\) that needs to be filtered. These images can be grayscale or color, but they must have the same dimensions.
         - Additionally, the guided filter typically requires two parameters: the filter radius \(r\) and the regularization parameter \(\epsilon\).
      
      2. **Local Linear Model**:
         - At each pixel location \(i\), the guided filter constructs a local linear model to estimate the output pixel value.
         - The local model is based on a window of pixels centered around \(i\) with a radius \(r\). Within this window, the guided filter calculates the mean \(I_i\) and covariance \(\text{cov}(I_i, P_i)\) of the guidance image and the target image.
         - Using these statistics, the guided filter computes the slope and intercept of the linear model that best fits the relationship between the guidance image and the target image.
      
      3. **Filtering**:
         - Once the local linear model is established, the guided filter applies it to each pixel in the target image \(P\) to obtain the filtered output.
         - For each pixel \(i\) in the target image, the guided filter computes a weighted average of the target pixel values within the local window.
         - The weights for the averaging process are determined by the similarity between the guidance image values in the window and the guidance value at pixel \(i\). Higher similarity results in higher weights, indicating stronger influence on the filtered output.
         - By incorporating the local linear model and using adaptive weights based on guidance image similarity, the guided filter effectively smooths the target image while preserving important edges and structures.
      
      4. **Regularization**:
         - To stabilize the filtering process and prevent overfitting to noisy or textured regions, the guided filter applies regularization.
         - The regularization parameter \(\epsilon\) controls the amount of smoothing applied to the output. A higher value of \(\epsilon\) results in stronger regularization and more smoothing, while a lower value preserves finer details.
      
      5. **Output**:
         - The result of the guided filter is a smoothed version of the target image \(P\), where noise is reduced and important structures are preserved.
         - The guided filter is particularly effective for tasks like edge-preserving smoothing, detail enhancement, and HDR tone mapping, where maintaining visual fidelity is essential.

4. **Dark Channel Prior (DCP) Algorithm**:
    - **Purpose**: Haze or turbidity in underwater environments can significantly degrade image quality by reducing contrast and visibility. The DCP algorithm aims to estimate and remove this haze, enhancing visibility and improving the overall quality of underwater images.
    - **Actions**:
        - Adapts the DCP algorithm to underwater conditions, considering factors such as water clarity, light scattering, and depth-dependent attenuation.
        - Estimates the transmission map and atmospheric light to effectively dehaze underwater images, revealing details hidden by haze or turbidity.

      1. **Dark Channel Calculation**:
         - The first step in the DCP algorithm is to compute the dark channel of the input image. The dark channel represents the minimum intensity value across a local patch for each pixel in the image.
         - The dark channel is computed using a sliding window approach, where for each pixel \(i\), the minimum intensity value within a local patch centered around \(i\) is determined.
         - Mathematically, the dark channel \(J_{dark}(i)\) at pixel \(i\) is computed as:
           \[J_{dark}(i) = \min_{p \in \text{patch}(i)}(\min_{c \in \text{channels}}(J(p)_c))\]
         where \(J(p)_c\) represents the intensity value of channel \(c\) at pixel \(p\), and \(\text{patch}(i)\) denotes the local patch centered around pixel \(i\).
      
      2. **Atmospheric Light Estimation**:
         - Once the dark channel is computed, the next step is to estimate the atmospheric light, which represents the light scattered by particles in the scene.
         - The atmospheric light is estimated based on the principle that in outdoor scenes, the dark channel tends to have low values in regions corresponding to sky or haze, and higher values in non-haze regions.
         - The DCP algorithm selects the top \(0.1\%\) of pixels with the highest intensity values in the dark channel as candidates for atmospheric light estimation.
         - From these candidate pixels, the pixel with the highest intensity value in the original input image is chosen as the atmospheric light.
      
      3. **Transmission Map Calculation**:
         - With the dark channel and atmospheric light estimated, the next step is to compute the transmission map, which represents the proportion of scene radiance that reaches the camera.
         - The transmission map \(t(i)\) at each pixel \(i\) is computed using the following equation:
           \[t(i) = 1 - \omega \times \min_{c \in \text{channels}}(\frac{J(i)_c}{A_c})\]
         where \(J(i)_c\) represents the intensity value of channel \(c\) at pixel \(i\), \(A_c\) represents the atmospheric light intensity value for channel \(c\), and \(\omega\) is a parameter controlling the amount of haze removal.
      
      4. **Image Dehazing**:
         - Finally, the dehazing process involves using the transmission map to attenuate the haze in the original input image.
         - The dehazed image \(I_{dehazed}\) at each pixel \(i\) is computed as:
           \[I_{dehazed}(i) = \frac{I(i) - A}{\max(t(i), t_0)} + A\]
         where \(I(i)\) represents the intensity value of the original input image at pixel \(i\), \(A\) represents the atmospheric light intensity, and \(t_0\) is a small constant to prevent division by zero.
         
5. **Scene Radiance Recovery**:
    - **Purpose**: After removing haze and noise, scene radiance recovery aims to restore the natural appearance of underwater scenes by adjusting pixel values based on the estimated transmission map and atmospheric light.
    - **Actions**:
        - Recovers the original radiance of underwater scenes by compensating for the attenuation of light at different depths and enhancing visibility, resulting in clearer and more visually appealing underwater images.

By following this aligned pipeline tailored to underwater dehazing, the code aims to enhance the quality and visibility of underwater images, revealing details and colors that may be obscured by haze, noise, or color distortion.
