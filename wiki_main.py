
import requests
from bs4 import BeautifulSoup

class WikiWorker:
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        
    @staticmethod
    def _extract_company_symbol(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        if not table:
            print('Table with id "constituents" not found')
            return []
        
        table_rows = table.find_all('tr')
        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip()
            yield symbol
    
    def get_sp_500_companies(self):
        try:
            response = requests.get(self._url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data: {e}')
            return []
        
        return self._extract_company_symbol(response.text)


if __name__ == "__main__":
    worker = WikiWorker()
    for company in worker.get_sp_500_companies():
        print(company)

    
    