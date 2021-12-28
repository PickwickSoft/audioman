import sys
import requests
import re

table_pattern = (r"(\s<tr>\n"
                 r"\s+<td>client</td>\n"
                 r"\s+<td>yes</td>\n"
                 r"\s+<td>\S{11}</td>)")

id_section_pattern = r"<td>\S{11}</td>"


def get_api_key() -> str:
    """
    Because of broken O-Auth audioman gets the generated API key from acoustid.org website

    :return: API Key
    """
    url = 'https://acoustid.org/webservice'
    html = requests.get(url)
    match = re.search(table_pattern, html.text)
    if match:
        match = re.search(id_section_pattern, match.group())
        if match:
            return match.group().replace("<td>", "").replace("</td>", "")
    else:
        print("No API Key found", file=sys.stderr)
