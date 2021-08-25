import csv
import requests
import json


class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getCurrentCoinPrice(asset):
    response = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+asset+'&tsyms=USD')
    return response.json()['USD']

def getDollarCostAverageWithoutFees(asset, tax, headers, data):
    
    assetIndex = headers.index('Asset')
    transactionTypeIndex = headers.index('Transaction Type')
    usdTotalIndex = headers.index('USD Total (inclusive of fees)')
    quantityTransactedIndex = headers.index('Quantity Transacted')

    total = 0
    numShares = 0

    for row in data:
        if row[assetIndex] == asset and row[transactionTypeIndex] == 'Buy':
            #print(row)
            total += float(row[usdTotalIndex])
            numShares += float(row[quantityTransactedIndex])

    if numShares > 0 and total > 0:
        dca = (total / numShares)
        currentAssetPrice = getCurrentCoinPrice(asset)

        currentUSDValue = (currentAssetPrice * numShares)
        usdGainLoss = (currentUSDValue - total)
        pctGainLoss = ((usdGainLoss / total) * 100)
        taxesOwed = (usdGainLoss * tax)
        takeHome = (usdGainLoss - taxesOwed)

        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}### {asset} REPORT ###{bcolors.ENDC}\n')
        print(f'You purchased {bcolors.WARNING}{numShares}{bcolors.ENDC} ({bcolors.WARNING}${total:.2f} USD{bcolors.ENDC}) units of {asset} for an average of {bcolors.WARNING}${dca:.2f} USD{bcolors.ENDC} per share.\n')
        print(f'{bcolors.OKCYAN}Amount Bought:\t\t{bcolors.ENDC} {numShares}')
        print(f'{bcolors.OKCYAN}Average Price Paid:\t{bcolors.ENDC} {dca:.2f}')
        print(f'{bcolors.OKCYAN}Current Price:\t\t{bcolors.ENDC} {currentAssetPrice:.2f}')
        print(f'{bcolors.OKCYAN}Total USD Paid:\t\t{bcolors.ENDC} {total}')
        print(f'{bcolors.OKCYAN}Current USD Value:\t{bcolors.ENDC} {(currentUSDValue):.2f}')
        print(f'{bcolors.OKCYAN}USD Gain/Loss:\t\t{bcolors.ENDC} {(usdGainLoss):.2f}')
        print(f'{bcolors.OKCYAN}PCT Gain/Loss:\t\t{bcolors.ENDC} {(pctGainLoss):.2f}')
        print(f'{bcolors.OKCYAN}Amount Taxes Owed:\t{bcolors.ENDC} {bcolors.FAIL}{(taxesOwed):.2f}{bcolors.ENDC}')
        print(f'{bcolors.OKCYAN}Take Home:\t\t{bcolors.ENDC} {bcolors.OKGREEN}{(takeHome):.2f}{bcolors.ENDC}\n\n')
    else:
        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}### {asset} REPORT ###{bcolors.ENDC}\n')
        print(f'{bcolors.FAIL}Sorry, we didnt find any purchase history for {asset}{bcolors.FAIL}\n\n')

def main():

    transactionHistory = open('coinbase-history.csv', 'r')
    reader = csv.reader(transactionHistory)
    headers = next(reader, None)

    config = json.load(open('config.json', 'r'))
    assetArray = config['assets'].split(',')
    taxPercentage = float(config['tax_percentage'])

    if taxPercentage > 1:
        print(f'{bcolors.FAIL}Your tax_percentage must be in decimal form example: 0.22')
    
    else:
        
        for item in assetArray:
            getDollarCostAverageWithoutFees(item, taxPercentage, headers, reader)
            transactionHistory.seek(0)

    


if __name__ == "__main__":
    main()