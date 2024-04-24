import pdf_text_extraction
import ocr_text_extraction
import image_processing

if __name__ == "__main__":
    pdf_file_path = "book.pdf"
    json_output_path = "book_text.json"

    extracted_text = pdf_text_extraction.extract_text_from_pdf(pdf_file_path)
    pdf_text_extraction.save_to_json(extracted_text, json_output_path)
    print(f"Text extracted from {len(extracted_text)} pages and saved to {json_output_path}")

    folder_path = "listening-B1-trainer-part-2_-3_-4"
    image_processing.convert_folder_images_to_pdf(folder_path)
  
