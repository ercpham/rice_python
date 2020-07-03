import requests
import re
from bs4 import BeautifulSoup

base_URL = 'https://www.biblegateway.com/passage/?search='
q_version = '&version=NASB'

verse_string = input('What verse do you want to lookup? \n')

q_verse = verse_string.replace(' ', '+').replace(':', '%3A')

URL = base_URL + q_verse + q_version

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

html_text = soup.find(class_="passage-content passage-class-0")
verse_texts = html_text.findAll('p')

for verse in verse_texts:
    if "Copyright" in verse.text:
        continue
    clean_text = re.sub('(\[..\])|(\[.\])|[0-9]|\*', '', verse.text.strip())
    print(clean_text[1:])
    print()


#print(URL)

# book, address = verse_string.split(" ")
# chapter, verse = address.split(":")

# print(book, chapter, verse)