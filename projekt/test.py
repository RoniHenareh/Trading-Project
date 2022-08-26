#test

import yfinance as yf
from yfinance import ticker

x = input('Ange en aktie-ticker på NASDAQ börsen: ')
# felhantering måste göras

# yf.Ticker(x).info är en dic 
#definera om, för långt

# visar alla nycklar och värden

for nyckel in yf.Ticker(x).info.keys():
        if nyckel != ' ':
            print(nyckel, '=', yf.Ticker(x).info[nyckel])
        else:
            print('slut')

'''
def ger_beta(x):

    for nyckel in yf.Ticker(x).info.keys():
        beta = yf.Ticker(x).info['beta']
        break # beta är inte nåbar annars
        
    return beta

print('beta=', ger_beta(x))


def ger_namn(x):

    for nyckel in yf.Ticker(x).info.keys():
        namn = yf.Ticker(x).info['shortName']
        break
    return namn

print('företaget=', ger_namn(x))

def forward_pe(x):
    for nyckel in yf.Ticker(x).info.keys():
        fpe = yf.Ticker(x).info['forwardPE']
        break
    return fpe

print('fpe=', forward_pe(x))

def trailing_pe(x):
    for nyckel in yf.Ticker(x).info.keys():
        tpe = yf.Ticker(x).info['trailingPE']
        break
    return tpe

print('tpe', trailing_pe(x))


def ps(x):
    for nyckel in yf.Ticker(x).info.keys():
        fps = yf.Ticker(x).info['priceToSalesTrailing12Months']
        break
    return fps

print('ps=', ps(x))

#soliditet kvar för fundamental analys.
'''

#['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
'''
def högsta(x):

    period = input('\nange ett tidsintervall på 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n för att ta reda på högsta priset: ')
    y = yf.Ticker(x).history(period)
    return max(list(y['High']))

print('\nhögsta värdet för perioden =', högsta(x), 'kr')

def lägsta(x):

    period = input('\nange ett tidsintervall på 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n för att ta reda på lägsta priset: ')
    y = yf.Ticker(x).history(period)
    return min(list(y['Low']))

print('\nlägsta värdet för perioden =', lägsta(x), 'kr')

def skillnad(x): 

    period = period = input('\nange ett tidsintervall på 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n för att ta reda den procentuella skillnaden mellan det högsta och lägsta priset: ')
    y = yf.Ticker(x).history(period)
    hög = max(list(y['High']))
    låg = min(list(y['Low']))
    
    return ((hög-låg)/hög) * 100

print('\nden procentuella skillnaden är',skillnad(x), '%')'''






