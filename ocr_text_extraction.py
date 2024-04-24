import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    num_pages = doc.page_count

    text_by_page = {}
    for page_num in range(num_pages):
        page = doc[page_num]

        # Convert page to image
        image = page.get_pixmap()
        img = Image.frombytes("RGB", [image.width, image.height], image.samples)

        # Use OCR to extract text from the image
        text_by_page[page_num + 1] = pytesseract.image_to_string(img, lang='eng')

    doc.close()
    return text_by_page

def save_to_json(data, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
