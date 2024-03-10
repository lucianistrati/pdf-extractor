import PyPDF2
import json

#
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#         num_pages = len(pdf_reader.pages)
#
#         text_by_page = {}
#         for page_num in range(num_pages):
#             page = pdf_reader.pages[page_num]
#             extracted_text = page.extract_text()
#             print(extracted_text)
#             text_by_page[page_num + 1] = extracted_text
#
#     return text_by_page
import fitz  # PyMuPDF


# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     num_pages = doc.page_count
#
#     text_by_page = {}
#     for page_num in range(num_pages):
#         page = doc[page_num]
#         text_by_page[page_num + 1] = page.get_text()
#         print(page.get_text())
#
#     doc.close()
#     return text_by_page

# import pytesseract
# from pillow import Image


# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     num_pages = doc.page_count
#
#     text_by_page = {}
#     for page_num in range(num_pages):
#         page = doc[page_num]
#
#         # Convert page to image
#         image = page.get_pixmap()
#         img = Image.frombytes("RGB", [image.width, image.height], image.samples)
#
#         # Use OCR to extract text from the image
#         text_by_page[page_num + 1] = pytesseract.image_to_string(img, lang='eng')
#
#     doc.close()
#     return text_by_page
#
#
# def save_to_json(data, json_path):
#     with open(json_path, 'w', encoding='utf-8') as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
#     pdf_file_path = "book.pdf"
#     json_output_path = "book_text.json"
#
#     extracted_text = extract_text_from_pdf(pdf_file_path)
#     save_to_json(extracted_text, json_output_path)
#
#     print(f"Text extracted from {len(extracted_text)} pages and saved to {json_output_path}")


# convert odt file to multiple images at:
#

import os
import cv2  # installation: pip install opencv-python


def process_grayscale_image(input_path, output_path, threshold=180):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded_img = cv2.threshold(img, threshold, 250, cv2.THRESH_BINARY)
    cv2.imwrite(output_path, thresholded_img)


def main():
    i = 0
    # folder_path = "test-Xmas-Trainer-B1"
    # folder_path = "Christmas-TRainer-B1"
    folder_path = "listening-B1-trainer-part-2_-3_-4"
    for file in os.listdir(folder_path):
        if file.startswith("img_"):
            continue
        filepath = os.path.join(folder_path, file)
        process_grayscale_image(filepath, os.path.join(folder_path,
                                                       f"img_{i}.png"))
        i += 1


if __name__ == "__main__":
    main()


# merge resulting images into one pdf at: https://png2pdf.com
