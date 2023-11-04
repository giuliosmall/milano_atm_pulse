from bs4 import BeautifulSoup
from endpoint import get_page

SELECTOR = "slwp_ctl00_PlaceHolderMain_SummaryLinkFieldControl2_SummaryLinkFieldControl2 > tbody > tr > td > div.item > div.link-item > a"

def get_news():
    data = get_page()
    soup = BeautifulSoup(data, 'html.parser')
    
    items = soup.select(SELECTOR)
    extracted_news = []
    print(items)

    for item in items:
        url = item.get('href', '')
        text = item.get_text(strip=True)
        extracted_news.append({
            'url': url,
            'text': text
        })
    
    print (extracted_news)


get_news()

