import requests
import datetime as dt
import matplotlib.pyplot as plt
def crypto_crncy_price(symbol, comparison_symbol = 'USD', all_data=True, aggregate=1,limit = 1, exchange=''):
    a = int(input('1 for Minute\n2 for Hourly\n3 for Today '))
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'.format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if a == 1: limit = 9999; url = url.replace('&limit=1', '&limit={}'.format(limit))
    elif a == 2: limit = 9999; url = url.replace('histominute','histohour'); url = url.replace('&limit=1', '&limit={}'.format(limit))
    elif a == 3: limit = 1; url = url.replace('histominute','histoday'); url = url.replace('&limit=1', '&limit={}'.format(limit))
    if all_data and a == 3: url += '&allData=true'
    if exchange: url += '&e={}'.format(exchange)
    a = requests.get(url).json()['Data']
    b = [(a[i]['time'], a[i]['close'], dt.datetime.fromtimestamp(a[i]['time'])) for i in range(len(a))]
    plt.plot([i[2] for i in b], [i[1] for i in b])
    plt.xticks(rotation = 30)
    plt.show()
    
# function testing: 
a = print(crypto_crncy_price('btc'))
b = print(crypto_crncy_price('eth'))
c = print(crypto_crncy_price('neo'))
d = print(crypto_crncy_price('neo', 'pkr'))
for i in a,b,c,d: print(i)
