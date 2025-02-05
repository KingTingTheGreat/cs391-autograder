from urllib.parse import urlparse
from requests import get
import pymupdf

TEXT_FILE = "/autograder/source/input_file.txt"
PDF_FILE ="/autograder/source/input_file.pdf"

def is_valid_url(url) -> bool:
    res = get(url)
    return res.ok

def is_from_domain(url, domain) -> bool:
    parsed_url = urlparse(url)
    if parsed_url.hostname is not None:
        return parsed_url.hostname.lower().endswith(domain)
    return False

def get_url_from_list(url_list, domain, msg="COULD NOT FIND URL") -> str:
    for url in url_list:
        if is_from_domain(url, domain):
            return url
    raise Exception(msg)

def list_from_file() -> list[str]:
    try:
        with open(TEXT_FILE, "r") as f:
            text = f.read().strip() 
            return text.split()
    except:
        with pymupdf.open(PDF_FILE) as doc:
            text = chr(12).join([page.get_text() for page in doc])
            return text.split()






















