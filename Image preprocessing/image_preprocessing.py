# -*- coding: utf-8 -*-
"""Image_Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clynmILRx04lOTi234NBHwHMWHxdMcHt

#Libraries
"""

import os
import cv2
import numpy as np

"""# Preprocessing function
 It preprocess the images to reduce the noises and resize in the images to be prepared for detection model
"""

def preprocess_function(img, target_size=(640, 640)):

    # Resize the image to the target_size which is the default size for the yolov5 detection model
    img_resized = cv2.resize(img, target_size)

    # Apply median blur to remove salt and pepper noise
    img_median = cv2.medianBlur(img_resized, 5)

    # Apply Gaussian blur to remove Gaussian noise
    img_processed = cv2.GaussianBlur(img_median, (5, 5), 0)

    return img_processed

def preprocess_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = os.listdir(input_folder)

    for image_file in image_files:
        # Read the image
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)

        # Check if the image was successfully read
        if img is not None:
            # Preprocess the image
            processed_img = remove_noise(img)

            # Save the processed image in the output folder
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, processed_img)
            print(f"Processed image saved: {output_path}")
        else:
            print(f"Error reading image: {image_path}")

# Usage example
input_folder = '/content/input'
output_folder = '/content/output'
preprocess_images(input_folder, output_folder)