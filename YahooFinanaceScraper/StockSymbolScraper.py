import requests
from lxml import html

UK_url = 'https://finance.yahoo.com/screener/unsaved/2517abff-69c8-425d-93fc-97b00cb5f622?count=100&offset='
USA_book_value_gt_1_url = 'https://finance.yahoo.com/screener/unsaved/4800afee-7950-498c-8572-a53a19c010e1?count=100&offset='
USA_book_value_lt_1_url = 'https://finance.yahoo.com/screener/unsaved/da8bc3b1-d471-4974-869f-6eaea77b2c95?count=100&offset='
urls = [UK_url, USA_book_value_gt_1_url, USA_book_value_lt_1_url]
s = requests.Session()

def getSymbols(url):
    symbols = list()
    offset = 0
    while(True):
        page = s.get(url + str(offset))
        tree = html.fromstring(page.content)


        if not tree.xpath('//a[@class="Fw(600) C($linkColor)"]/text()'):
            print(symbols)
            break

        symbols += tree.xpath('//a[@class="Fw(600) C($linkColor)"]/text()')
        offset += 100
        
        try:
            time.sleep(0.5)
        except:
            continue

    return symbols


symbols = list()

for url in urls:
    symbols += getSymbols(url)


with open("symbols", "w") as output:
    for symbol in symbols:
        if not symbol.endswith('.IL'):
            output.write("%s\n" % symbol)
