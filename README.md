# Milano ATM Pulse

Milano ATM Pulse is a Python tool for scraping the latest news and updates from Milan's public transportation services, provided by the website www.atm.it.

## Disclaimer

This project is **not affiliated, associated, authorized, endorsed by, or in any way officially connected** with Azienda Trasporti Milano (ATM), or any of its subsidiaries or affiliates. The official ATM website can be found at [www.atm.it](https://www.atm.it).

## Features

- Scrape real-time news and updates from www.atm.it.
- Utilizes BeautifulSoup to parse HTML content.
- Fetches updates on Milan's public transport for residents, commuters, and visitors.

## Installation

To use MilanTransitNewsScraper, you need Python 3.x and `pip`. Clone the repository and install the required packages:

```bash
git clone https://github.com/giuliosmall/milano_atm_pulse.git
cd milano_atm_pulse
pip install -r requirements.txt
```

## Usage

Run `app.py`:

```bash
python app.py
```

### API Reference

Below is a brief overview of the API functions and its API endpoints:

- `/api/service` - Performs a health check of the API.
- `/api/status` - Retrieves the current status of the underground lines.
- `/api/traffic` - Provides planned traffic updates.
- `/api/news` - Fetches the latest news from the ATM newsroom.

Each endpoint returns data in a JSON format.

### Using the Endpoints

To use an endpoint, send a HTTP request to the URL composed of your application's base URL followed by the endpoint path.

For example:

```bash
curl http://http://127.0.0.1:5000/api/status
```

#### Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)




