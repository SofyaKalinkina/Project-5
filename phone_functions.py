import gdown
import pandas as pd

def download_file(url, output):
    gdown.download(url, output, quiet=False)

def clean_phone(phone):
    return ''.join(filter(str.isdigit, str(phone)))