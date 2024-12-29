# import requests
# from bs4 import BeautifulSoup

# url = "https://medium.com/@akikutvonen/how-to-train-sentencepiece-tokenizers-for-any-language-with-large-data-pretrained-models-for-e84bb225ed4a"

# response = requests.get(url)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, "html.parser")

# content_divs = soup.find_all('p')
# if content_divs:
#     text_content = "\n".join([p.get_text().strip() for p in content_divs])
#     with open("medium.txt", "a", encoding="utf-8") as file:
#         file.write(text_content)
# print("Done")
# url = 'https://medium.com/@akikutvonen/how-to-train-sentencepiece-tokenizers-for-any-language-with-large-data-pretrained-models-for-e84bb225ed4a'


import requests
from bs4 import BeautifulSoup

r = requests.get('https://medium.com/@akikutvonen/how-to-train-sentencepiece-tokenizers-for-any-language-with-large-data-pretrained-models-for-e84bb225ed4a')
# r = requests.get('https://study.com/learn/lesson/central-processing-unit-parts-function.html')
# parsing HTML content
soup = BeautifulSoup(r.content, 'html.parser')
content_divs = soup.find_all('p')
text_content = "\n".join([p.get_text().strip() for p in content_divs])
print(text_content)
