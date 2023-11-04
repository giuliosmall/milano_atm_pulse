from bs4 import BeautifulSoup
from endpoint import get_page

SELECTOR = "#cbqwp_ctl00_SPWebPartManager1_g_c8e995f5_72a5_4f90_88dd_ae34a9352dfa div.news-item a"

def get_traffic():
    data = get_page()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.select(SELECTOR)
    return [{"url": item.get('href', ''), "text": item.get_text(strip=True)} for item in items]
