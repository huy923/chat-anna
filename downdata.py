import requests
from bs4 import BeautifulSoup

# url = "https://wiki.archlinux.org/title/Special:Random"
url = "https://en.wikipedia.org/wiki/Special:Random"


count = 100

while count > 0:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    current_url = response.url
    with open("checkdata.txt","a+", encoding="utf-8") as file_check:
        if current_url not in file_check.read():
            file_check.write(f"{current_url}\n")
            content_divs = soup.find_all('p')
            # content_divs = soup.find_all('div', class_='content')
            # content_p = content_divs.find_all('p')
            if content_divs:
                text_content = "\n".join([p.get_text().strip() for p in content_divs])
                with open("./data/archwiki_pages.txt", "a", encoding="utf-8") as file:
                    file.write(text_content)
            count -= 1 

print("DONE")
