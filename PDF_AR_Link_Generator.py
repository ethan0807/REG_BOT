import Globals
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

# Generates the list of links to the PDFs of Army Regulations by crawling the Army Publishing Directorate website

globals = Globals.Defaults

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
main_url = 'https://armypubs.army.mil/ProductMaps/PubForm/AR.aspx'
links_file = globals.pdf_links_file


def find_and_write_pdf_links(url):
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.search(r'\/DR_pubs\/DR_a\/pdf\/web\/.*\.pdf$', href, re.I):
                pdf_link = urllib.parse.urljoin(url, href).strip()
                write_link_to_file(pdf_link)
                print(pdf_link)
    except requests.exceptions.RequestException:
        print(f"An error occurred with URL: {url}")
    return None


def find_pdf_links(main_url):
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(main_url, headers=headers, verify=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    pub_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if re.search(r'Details\.aspx\?PUB_ID=\d+$', href, re.I) and "CAC" not in href:
            full_url = urllib.parse.urljoin(main_url, href)
            pub_links.append(full_url)
            # print(f"Found link: {full_url}")
    return pub_links


def write_link_to_file(link):
    if link:
        # Write the content to a file
        with open(links_file, "a", encoding="utf-8") as file:
            file.write(link + "\n")
        print(f"Link : {link}")


# Create/Clear links file
with open(links_file, 'w'):
    pass
pub_links = find_pdf_links(main_url)
[find_and_write_pdf_links(link) for link in pub_links if link is not None]
