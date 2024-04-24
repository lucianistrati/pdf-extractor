import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text_by_page = {}
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text = page.extract_text()
            text_by_page[page_num + 1] = extracted_text

    return text_by_page
