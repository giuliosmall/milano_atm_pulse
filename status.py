from bs4 import BeautifulSoup
from endpoint import get_page

def get_line(row, selector="img"):
    element = row.select_one(selector)
    return element.get("title", '') if element else ''

def get_content(row, selector):
    text = row.select_one(selector)
    return text.get_text(strip=True) if text else ''

def get_rows(document):
    trs = document.select("#StatusLinee tr")
    return [e for e in trs if e.get_text(strip=True) and not e.select(".StatusLinee_mex") and not e.get('id')]

def get_status():
    data = get_page()
    soup = BeautifulSoup(data, 'html.parser')
    rows = get_rows(soup)
    return [{"line": get_line(row), "text": get_content(row, ".StatusLinee_StatoScritta"), "status": get_content(row, ".StatusLinee_StatoScritta")} for row in rows]
