# pdf-extractor

This repository contains code for extracting text from PDF documents using various techniques.

## Source Files

- `image_processing.py`: Contains functions for processing images extracted from PDF documents.
- `main.py`: Main script for orchestrating the PDF extraction process.
- `ocr_text_extraction.py`: Module for extracting text using Optical Character Recognition (OCR) techniques.
- `pdf_text_extraction.py`: Module for extracting text directly from PDF files.

## Usage

To use the PDF extraction functionalities provided by this repository, follow these steps:

1. Clone the repository:

```
git clone <repository-url>
cd pdf-extraction
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the main script to extract text from PDFs:

```
python main.py
```

## Dependencies

This project relies on the following Python packages:

- PyPDF2
- PyMuPDF
- pytesseract
- OpenCV (cv2)
- Pillow (PIL)

Install these dependencies using the provided `requirements.txt` file.
