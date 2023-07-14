import Globals
import os
import requests

# Downloads the PDFs from the list of URLs in the pdf_links.txt file

globals = Globals.Defaults
pdf_dir = globals.pdf_dir
pdf_links_file = globals.pdf_links_file

# Read the list of URLs from a file
with open(pdf_links_file, 'r') as f:
    urls = f.read().splitlines()

# Create directory if it does not exist
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# User Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Loop through each URL
for url in urls:
    # Determine the local filename
    local_filename = pdf_dir + url.split("/")[-1]

    # Only download the file if it has not already been downloaded
    if not os.path.isfile(local_filename):
        try:
            # Send a request to the URL
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()  # Raise exception if status is not 200

            # Write the content to a file
            with open(local_filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {url}")

        except Exception as e:
            # Log any exceptions to the console
            print(f"Exception occurred with {url}: {e}")
    else:
        print(f"File {local_filename} already exists. Skipping download.")
