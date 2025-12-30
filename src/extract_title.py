import re

TITLE_REGEX = re.compile(r"^#{1} .+$", flags=re.MULTILINE)

def extract_title(markdown: str) -> str:
    match = TITLE_REGEX.search(markdown)

    if match is None:
        raise ValueError("No title found in markdown")
    
    # Get the first match
    title = match.group(0)

    # Strip off the leading hashtag and any leading/training whitespace
    return title[1:].strip()
