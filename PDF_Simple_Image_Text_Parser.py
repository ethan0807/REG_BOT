import Globals
import fitz  # PyMuPDF
from google.cloud import vision
import os

# Extracts text from images in the PDFs using Google Vision API. Not currnetly used. May be used in the future to improve the semantic search.

# Must set google api credentials in os environment first. ex: "setx GOOGLE_APPLICATION_CREDENTIALS <path_to_json_cred_file>"

globals = Globals.Defaults
pdf_dir = globals.pdf_dir
output_dir = './data/parsed_image_text/'

# Initialize Google Vision client
client = vision.ImageAnnotatorClient()

# Counter for the number of API calls
api_call_counter = 0

# Check if the output directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def get_pdf_list():
    pdf_paths = []  # This list will store the full paths of PDFs

    # Loop through each file in the PDF directory
    '''
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            # Full path of the PDF file
            pdf_path = os.path.join(pdf_dir, filename)
            pdf_paths.append(pdf_path)  # Add the full path of PDF to the list
    '''
    # For Testing
    # Property Management
    pdf1 = '.\\data\\pdfs\\r735-5_Web_Final.pdf'
    # Officer Transfer and Discharges
    pdf2 = '.\\data\\pdfs\\ARN3140_AR600-8-24_FINAL.pdf'
    # Child Development Services
    pdf3 = '.\\data\\pdfs\\ARN3218_AR608-10_Web_FINAL.pdf'
    # Material Mantienance Management
    pdf4 = '.\\data\\pdfs\\ARN32929-AR_750-1-000-WEB-1.pdf'
    pdf_paths.append(pdf1)
    pdf_paths.append(pdf2)
    pdf_paths.append(pdf3)
    pdf_paths.append(pdf4)
    return pdf_paths

# Function to extract text from an image using Google Vision API


def extract_text_from_image(image):
    global api_call_counter
    image = vision.Image(content=image)
    response = client.text_detection(image=image)
    api_call_counter += 1
    print(f'Number of API calls: {api_call_counter}')
    texts = response.text_annotations
    if texts:
        return texts[0].description
    return ""


# Simple filter for image text. Will rely on the LLM to do the heavy lifting in determing what is meaningful.


def filter_image_text(image_text):
    lines = image_text.split('\n')
    filtered_lines = [line for line in lines if len(
        line) >= 10 and any(c.isalpha() for c in line)]
    filtered_text = '\n'.join(filtered_lines)
    return filtered_text

# Find and parse out the line of text that holds the figure id.


def get_figure_id_line(img, page):
    # Get the rectangle of the image
    img_rect = page.get_image_bbox(img)

    # Define a small region just below the image (50 units in PyMuPDF's coordinate system)
    search_rect = fitz.Rect(
        img_rect.x0, img_rect.y1, img_rect.x1, img_rect.y1 + 50)

    # Extract the text in this region
    search_text = page.get_textbox(search_rect)

    # Search for the first line of text that starts with "Figure" (case insensitive)
    figure_id_line = next((line for line in search_text.splitlines(
    ) if line.lower().startswith("figure")), None)
    return figure_id_line

# Main function


def main():
    for pdf in get_pdf_list():

        text_file = output_dir + 'images_text_' + \
            os.path.splitext(os.path.basename(pdf))[0] + '.txt'
        # Create/Clear image text file
        with open(text_file, 'w', encoding="utf-8"):
            pass
        doc = fitz.open(pdf)
        for page in doc:
            image_list = page.get_images(full=True)
            for img in image_list:
                base_image = doc.extract_image(img[0])
                image_text = filter_image_text(
                    extract_text_from_image(base_image['image']))

                with open(text_file, "a", encoding="utf-8") as file:
                    file.write(image_text)

    print(f'Total API calls made: {api_call_counter}')


main()
