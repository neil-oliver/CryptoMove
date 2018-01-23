import operator
import requests

#mimumum amount, transaction fee
exchanges = {
    "GDAX" : {
        "name": "GDAX",
        "trading_fee": 0.003,
        "currencies": {
            "BTC":(0,0),
            "BCH":(0,0),
            "ETH":(0,0),
            "LTC":(0,0)
        }
    },

    "Binance" : {
        "name" : "Binance",
        "trading_fee": 0.001,
        "currencies" : {
            "BNB" : (2,0.71),
            "BTC" : (0.002,0.001),
            "NEO" : (1,0),
            "ETH" : (0.1,0.01),
            "LTC" : (0.02,0.01),
            "QTUM" : (0.02,0.01),
            "EOS" : (1.4,1),
            "SNT" : (20,32),
            "BNT" : (2.4,1.6),
            "GAS" : (0.001,0),
            "BCC" : (0.002,0.001),
            "BTM" : (10,5),
            "USDT" : (100,22),
            "HCC" : (0.001,0.0005),
            "HSR" : (0.001,0.0001),
            "OAX" : (12,9.6),
            "DNT" : (120,62),
            "MCO" : (0.6,0.91),
            "ICN" : (4,3.9),
            "ZRX" : (20,6.3),
            "OMG" : (0.6,0.58),
            "WTC" : (0.8,0.5),
            "LRC" : (24,11.1),
            "LLT" : (2,54.3),
            "YOYOW" : (20,47),
            "TRX" : (250,124),
            "STRAT" : (0.002,0.1),
            "SNGLS" : (40,47),
            "ETHOS" : (4,1.5),
            "KNC" : (4,3.2),
            "SNM" : (40,28),
            "FUN" : (160,92),
            "LINK" : (20,13.8),
            "XVG" : (0.2,0.1),
            "CTR" : (14,6.7),
            "SALT" : (0.8,1.3),
            "MDA" : (4,5.3),
            "MIOTA" : (10,0.5),
            "SUB" : (8,7.3),
            "ETC" : (0.02,0.01),
            "MTL" : (1,2.3),
            "MTH" : (70,34),
            "ENG" : (10,2.2),
            "AST" : (20,10.2),
            "DASH" : (0.004,0.002),
            "BTG" : (0.002,0.001),
            "EVX" : (5,2.7),
            "REQ" : (30,16.9),
            "VIB" : (40,30),
            "POWR" : (10,9.2),
            "ARK" : (0.2,0.1),
            "XRP" : (22,0.25),
            "MOD" : (4,2),
            "ENJ" : (160,43),
            "STORJ" : (6,6.8),
            "VEN" : (10,1.9),
            "KMD" : (0.004,0.002),
            "RCN" : (40,36),
            "NULS" : (6,1.9),
            "RDN" : (0.6,2.2),
            "XMR" : (0.1,0.04),
            "DLT" : (30,14.2),
            "AMB" : (20,16.2),
            "BAT" : (30,18),
            "ZEC" : (0.01,0.005),
            "BCPT" : (28,13.4),
            "ARN" : (14,3.7),
            "GVT" : (1,0.55),
            "CDT" : (70,87),
            "GXS" : (0.6,0.3),
            "POE" : (100,104),
            "QSP" : (60,21),
            "BTS" : (50,1),
            "XZC" : (0.04,0.02),
            "LSK" : (0.2,0.1),
            "TNT" : (70,56),
            "FUEL" : (120,46),
            "MANA" : (60,77),
            "BCD" : (2,1),
            "DGD" : (0.06,0.06),
            "ADX" : (4,5.2),
            "ADA" : (4,1),
            "PPT" : (0.4,0.24),
            "CMT" : (30,38),
            "XLM" : (21,0.01),
            "CND" : (400,62),
            "LEND" : (50,56),
            "WABI" : (8,3.6),
            "SBTC" : (2,1),
            "BCX" : (2,1),
            "WAVES" : (0.1,0.002),
            "TNB" : (140,92),
            "GTO" : (30,22),
            "ICX" : (2,1.3),
            "OST" : (30,19),
            "ELF" : (5,7.5),
            "AION" : (2,2),
            "BRD" : (8,6.9),
            "NEBL" : (0.1,0.01),
            "VIBE" : (20,10.7),
            "LUN" : (2,0.32),
            "RLC" : (10,4.8),
            "INS" : (2,2.2),
            "EDO" : (2,2.7),
            "WINGS" : (6,9.5),
            "NAV" : (0.4,0.2),
            "TRIG" : (10,6.9),
            "APPC" : (16,7.1)
        }
    },

    "Bitfinex" : {
        "name" : "Bitfinex",
        "trading_fee": 0.002,
        "currencies" : {
            "BTC" : (0,0.0008),
            "ETH" : (0,0.01),
            "XRP" : (0,0.02),
            "EOS" : (0,0.1),
            "NEO" : (0,0),
            "BCH" : (0,0.0001),
            "LTC" : (0,0.001),
            "MIOTA" : (0,0.5),
            "ETC" : (0,0.01),
            "XMR" : (0,0.04),
            "BTG" : (0,0),
            "DASH" : (0,0.01),
            "OMG" : (0,0.1),
            "ZEC" : (0,0.001),
            "SAN" : (0,0.1),
            "QTUM" : (0,0.01),
            "QASH" : (0,1),
            "ZRX" : (0,0),
            "SNT" : (0,0),
            "ETP" : (0,0.01),
            "TNB" : (0,0),
            "EDO" : (0,0.5),
            "DATA" : (0,1),
            "YOYOW" : (0,0.1),
            "FUN" : (0,0),
            "GNT" : (0,0),
            "MANA" : (0,0),
            "BAT" : (0,0),
            "SPANK" : (0,0),
            "AVT" : (0,0.5),
        }
    }
}


#update USD price to each currency of each exchange
def getUSD():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0")

    for currency in r.json():
        for exchange in exchanges:
            if currency['symbol'] in exchanges[exchange]["currencies"]:
                exchanges[exchange]["currencies"][currency['symbol']] += (currency['price_usd'],)

getUSD()


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

start = input("Please enter the name of the exchange you are transferring from: \n")

end = input("Please enter the name of the exchange you are transferring to: \n")

currency = input("please enter the code of the currency you are transferring. i.e. XRP: \n")

amount = float(input("Please enter the amount of currency you are transferring: \n"))

cheapestTransfer(exchanges[start], exchanges[end], amount, currency)
