import re

def strip_tags(title):
    return re.sub(r'(?i)(yo|mama|is|so|her|are|joke|jokes|
        and|[^\w]|^\s+)', '', title)
