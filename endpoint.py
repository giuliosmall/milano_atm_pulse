import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ENDPOINT = "https://www.atm.it/it/Pagine/default.aspx"

def get_page():
    response = requests.get(ENDPOINT, verify=False)
    return response.text
