import os

index_version = "v1"
texts_version = "v1"


class Defaults:
    
    default_model = "gpt-4" # chunk limit 8192 
    # "gpt-3.5-turbo"  chunk limit 4096
    # "text-davinci-003" chunk limit 4097
    # "ada"
    default_max_chunk_size = 2048
    default_temperature = 0.1

    index_path = "./data/index/" + index_version + "/"
    texts_path = "./data/parsed_sections/" + texts_version + "/"
    pdfs_path = "./data/pdfs/"
    open_api_key = os.environ["OPENAI_API_KEY"]
    pdf_dir = './data/pdfs/'
    pdf_links_file = pdf_dir + 'pdf_links.txt'
