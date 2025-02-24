import os
import fitz  # PyMuPDF

def update_pdf_metadata(folder_path):
    """
    Scans a folder and its subfolders for PDF files and updates their metadata title
    to match their respective filenames.
    
    :param folder_path: The root folder to scan.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                try:
                    doc = fitz.open(pdf_path)
                    metadata = doc.metadata
                    new_title = os.path.splitext(file)[0]  # Filename without extension
                    
                    # Update metadata
                    metadata["title"] = new_title
                    doc.set_metadata(metadata)
                    doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
                    doc.close()
                    
                    print(f"Updated metadata title for: {pdf_path}")
                except Exception as e:
                    print(f"Error processing {pdf_path}: {e}")

if __name__ == "__main__":
    folder_to_scan = "./pdfs"
    if os.path.isdir(folder_to_scan):
        update_pdf_metadata(folder_to_scan)
    else:
        print("Invalid folder path. Please enter a valid directory.")
