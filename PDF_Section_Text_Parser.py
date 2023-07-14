import Globals
import os
import re
import PyPDF2

# Generates the text files for each section of the PDFs in the pdfs directory

globals = Globals.Defaults()

sections_data_path = globals.texts_path
pdf_dir = globals.pdf_dir
pdf_paths = []


def get_pdf_list():
    # Uncomment only if you want to try and parse all PDFs in the PDF directory
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

    # Check if the output directory exists, if not, create it
    if not os.path.exists(sections_data_path):
        os.makedirs(sections_data_path)

    return pdf_paths


def get_regulation_number(text):
    # This regular expression matches the phrase "Army Regulation" followed by a space, then captures any characters that follow until a newline character is encountered.
    # The captured characters are the regulation number.
    match = re.search(r'Army Regulation ([^\n]*)', text)
    return match.group(1).replace('–', '-').replace(' ', '') if match else None


def check_valid_section(text):
    # Check if there are at least two lines in the section.
    return len(text.split('\n')) > 2


def get_section_details(text):
    pattern = r'\s*(\d+)\s*–\s*(\d+)\.\s*([^\n]*)'
    matches = re.match(pattern, text)

    if matches:
        section = f"{matches.group(1)}–{matches.group(2)}"
        title = matches.group(3).strip()
        return title, section
    else:
        return None, None


def get_filename(regulation_number, section_number, section_title):
    filename = f'AR{regulation_number}_{section_number}_{section_title}'
    # Replace spaces with underscores, then replace en dashes with hyphens.
    filename = filename.replace(' ', '_').replace('–', '-')
    # Remove spaces and any character that is not a word character (alphanumeric or underscore) or a hyphen.
    filename = re.sub(r'[^-\w]', '', filename.replace(' ', ''))
    filename = filename.replace('___', '_')
    filename = filename.replace('__', '_')

    return filename


def write_section_to_file(section_text, filename):
    with open(sections_data_path + filename + ".txt", 'w', encoding='utf-8') as f:
        f.write(section_text)


def remove_footer_text(text):
    # Attempt to remove the footer text that gets embedded in the section text
    # Not consistent through all pdfs so may be no perfect way to do this
    text = re.sub(r'\d+\s*AR\s*\d+–\d+\s*.\s*\d+\s*\w+\s*\d{4}', '', text)
    text = re.sub(
        r"(\d{1,2} (January|February|March|April|May|June|July|August|September|October|November|December) \d{4})", '', text)

    # Define the pattern for the text format
    pattern = r"^.*•\s*\d+\s*(?!\.)"

    # Split the multiline string into lines
    lines = text.split('\n')

    # Apply the regex substitution to each line
    new_lines = [re.sub(pattern, '', line) for line in lines]

    # Join the processed lines back into a multiline string
    new_text = '\n'.join(new_lines)

    pattern = r"^.*•\s*"

    # Split the multiline string into lines
    lines2 = new_text.split('\n')

    # Apply the regex substitution to each line
    new_lines2 = [re.sub(pattern, '', line) for line in lines2]

    # Join the processed lines back into a multiline string
    new_text2 = '\n'.join(new_lines2)

    return new_text2


def split_into_sections(text):
    return re.split(r'(\n\s*\d{1,2}\s*–\s*\d+\s*\.\s*.+)', text)


def remove_appendecies(text):
    # Define the pattern for the text format
    pattern = r"\s*Appendix A.*"

    # Substitute the matched pattern with an empty string
    return re.sub(pattern, '', text, flags=re.DOTALL)


def parse_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        regulation_number = None
        all_text = ''

        # Extract all text from the PDF into a single string.
        for i in range(num_pages):
            page_text = pdf_reader.pages[i].extract_text()
            # Remove the footer part from the page_text
            page_text = remove_footer_text(page_text)
            if i == 0:
                regulation_number = get_regulation_number(page_text)
            all_text += page_text

        all_text = remove_appendecies(all_text)
        # Split the text into sections based on section header.
        sections = split_into_sections(all_text)

        # Process each section.
        for i in range(1, len(sections), 2):
            section_text = sections[i] + sections[i + 1]

            if check_valid_section(section_text):
                section_title, section_number = get_section_details(
                    section_text)
                filename = get_filename(
                    regulation_number, section_number, section_title)
                source_text = f"Source: AR {regulation_number}, Section {section_number} {section_title}"
                write_section_to_file(section_text, filename)
            else:
                print(
                    f'Warning: Section {section_number} of {regulation_number} contains only one line of text and was not written to a file.')


if __name__ == "__main__":
    for pdf in get_pdf_list():
        parse_pdf(pdf)
