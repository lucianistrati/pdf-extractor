import os
import cv2

def process_grayscale_image(input_path, output_path, threshold=180):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded_img = cv2.threshold(img, threshold, 250, cv2.THRESH_BINARY)
    cv2.imwrite(output_path, thresholded_img)

def convert_folder_images_to_pdf(folder_path):
    i = 0
    for file in os.listdir(folder_path):
        if file.startswith("img_"):
            continue
        filepath = os.path.join(folder_path, file)
        process_grayscale_image(filepath, os.path.join(folder_path, f"img_{i}.png"))
        i += 1
