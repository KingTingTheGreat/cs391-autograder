from urllib.parse import urlparse
from requests import get

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

