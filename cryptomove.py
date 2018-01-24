import requests
from exchanges import exchanges

#update USD price to each currency of each exchange
def getUSD():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0")

    for currency in r.json():
        for exchange in exchanges:
            if currency['symbol'] in exchanges[exchange]["currencies"]:
                exchanges[exchange]["currencies"][currency['symbol']] += (currency['price_usd'],)

getUSD()


# calculate the cheapest way to transfer
def cheapestTransfer(fromExchange, toExchange, amount, startCurrency):

    fee = float(fromExchange["currencies"][startCurrency][2]) * fromExchange["currencies"][startCurrency][1]

    cheapest = ("",float("inf"))
    for currency in fromExchange["currencies"]:
        cheapFee = float(fromExchange["currencies"][currency][2]) * fromExchange["currencies"][currency][1]
        if cheapFee < cheapest[1] and currency in toExchange["currencies"]:
            cheapest = (currency, cheapFee)

    exchangeFee = float(fromExchange["currencies"][startCurrency][2]) * fromExchange["trading_fee"] * amount

    lowFee =  float(toExchange["currencies"][cheapest[0]][2]) * toExchange["currencies"][cheapest[0]][1]

    exchangeFee2 = float(toExchange["currencies"][startCurrency][2]) * toExchange["trading_fee"] * amount

    totalAlt = exchangeFee + exchangeFee2 - lowFee


    #Print out the results

    print("\nTransfer fee from " + fromExchange["name"] + " to " + toExchange["name"] + " in " + startCurrency + " will cost: $" + str(fee))

    print("\nSearching an alternative way of transferring...\n")

    print("Exchange fee from " + startCurrency + " to " + cheapest[0] + " at " + fromExchange["name"] + " will cost: $" + str(exchangeFee))

    print("Transfer fee from " + fromExchange["name"] + " to " + toExchange["name"] + " in " + cheapest[0] + " will cost: $" + str(lowFee))

    print("Exchange fee from " + cheapest[0] + " to " + startCurrency + " at " + toExchange["name"] + " will cost: $" + str(exchangeFee2))

    print("The total fee from exchanging to " + cheapest[0] + " before transferring to " + toExchange["name"] + " and then back again is $" + str(totalAlt))

    if fee > totalAlt:
        print("Converting to " + cheapest[0] + " before transferring to " + toExchange["name"] + " will save you $" + str(fee - totalAlt))
    else:
        print("Transferring to " + toExchange["name"] + " using " + startCurrency + " is the cheapest method.")


#start of main program

start = ""
while start not in exchanges:

    start = input("Please enter the name of the exchange you are transferring from: \n")

    if start not in exchanges:
        print("Error: Exchange not supported.")


end = ""
while end not in exchanges or end == start:

    end = input("Please enter the name of the exchange you are transferring to: \n")

    if end not in exchanges:
        print("Error: Exchange not supported.")

    if end == start:
        print("Your starting and ending exchanges seem to be the same.")

currency = ""
while currency not in exchanges[start]["currencies"]:

    currency = input("Please enter the code of the currency you are transferring. i.e. XRP: \n")

    if currency not in exchanges[start]["currencies"]:
        print("Error: currency code not found.")

while True:
    try:
        amount = float(input("Please enter the amount of currency you are transferring: \n"))

        if amount >= exchanges[start]["currencies"][currency][0]:
            cheapestTransfer(exchanges[start], exchanges[end], amount, currency)
        else:
            print("This number is below the minimum value for this currency.")

    except ValueError:
        print("This was not recognised as a number.")

