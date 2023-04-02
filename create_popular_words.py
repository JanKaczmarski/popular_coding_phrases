import requests
from bs4 import BeautifulSoup

URL = "https://www.codewizardshq.com/kids-guide-200-common-programming-terms/"
session_obj = requests.Session()
response = session_obj.get(URL, headers={"User-Agent": "Mozilla/5.0"})

html = response.content

soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

HTML = str(soup.contents[1])


def extract_from_tag(html_text: str, opening_tags: str, closing_tags: str):
    sol = []
    splitted_html = html_text.split(opening_tags)
    for part in splitted_html:
        splitted_part = part.split(closing_tags)
        if len(splitted_part[0].split()) == 1:
            sol.append(splitted_part[0])
    return sol


popular_words = extract_from_tag(HTML, '</p><h3>', '</h3><p>')

with open('popular_words.txt', 'w', encoding='UTF-8') as file:
    seq = ''
    for word in popular_words:
        seq += f"{word}\n"
    file.write(seq)
