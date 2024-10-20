import fitz  # PyMuPDF
import docx
import docx2txt
import requests

def extract_text_from_pdf(file_path):
    """
    Extract text from all pages of a PDF document.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: Extracted text from all pages of the PDF.
    """
    text = ""
    try:
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text("text")
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
    return text


def extract_text_from_docx(file_path):
    """
    Extract text from a .docx document.

    Args:
        file_path (str): The path to the .docx file.

    Returns:
        str: Extracted text from the .docx file.
    """
    text = ""
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error extracting DOCX text: {e}")
    return text


def extract_text_from_doc(file_path):
    """
    Extract text from a .doc document.

    Args:
        file_path (str): The path to the .doc file.

    Returns:
        str: Extracted text from the .doc file.
    """
    text = ""
    try:
        text = docx2txt.process(file_path)
    except Exception as e:
        print(f"Error extracting DOC text: {e}")
    return text


def download_file_from_url(url):
    local_filename = url.split('/')[-1]
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_filename
    else:
        raise Exception(f"Failed to download the file: {url}")