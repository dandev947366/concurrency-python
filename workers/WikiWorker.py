import requests
from bs4 import BeautifulSoup

class WikiWorker:
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        
    @staticmethod
    def _extract_company_symbols(page_html):
        """Extract company symbols from the Wikipedia page HTML."""
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        
        if not table:
            print('Table with id "constituents" not found')
            return []
        
        symbols = []
        table_rows = table.find_all('tr')[1:]  # Skip the header row
        
        for row in table_rows:
            cells = row.find_all('td')
            if cells:
                symbol = cells[0].get_text(strip=True)
                symbols.append(symbol)
        
        return symbols
    
    def get_sp_500_companies(self):
        """Fetch S&P 500 company symbols from Wikipedia."""
        try:
            response = requests.get(self._url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data: {e}')
            return []
        
        return self._extract_company_symbols(response.text)
