import pandas as pd

successful_requests = []
failed_requests = []

file1 = open('symbols', 'r') 
symbols = file1.readlines() 
for symbol in symbols:
    symbol = symbol.strip()
    print('Downloading Symbol:' + symbol)
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + symbol + "?period1=0&period2=1592438400&interval=1d&events=history"
    try:
        df = pd.read_csv(url)  
        df.head()
        df.to_csv('HistoricalData/'+ symbol+'.csv', index=False)
        successful_requests.append(symbol)
    except Exception as e:
        print(e)
        failed_requests.append(symbol)
        print("Request Failed")
        continue

print(failed_requests)

with open("FailedRequests", "w") as output:
    for symbol in failed_requests:
            output.write("%s\n" % symbol)

with open("SuccessfulRequests", "w") as output:
    for symbol in failed_requests:
            output.write("%s\n" % symbol)

