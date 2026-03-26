from ib_insync import IB, Stock

ib = IB()

def connect_ib():
    if not ib.isConnected():
        ib.connect('127.0.0.1', 7496, clientId=1)
    return ib

def get_ticker(symbol="AAPL"):
    contract = Stock(symbol, 'SMART', 'USD')
    ticker = ib.reqMktData(contract)
    return ticker