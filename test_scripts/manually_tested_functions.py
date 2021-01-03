# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:46:43 2020

@author: mling
"""

from XTConnect.Connect import XTSConnect
import pandas as pd

# Trading Interactive Creds
API_KEY = "ebaa4a8cf2de358e53c942"
API_SECRET = "Ojre664@S9"

# MarketData Creds
# API_KEY = "ebaa4a8cf2de358e53c942"
# API_SECRET = "Ojre664@S9"

XTS_API_BASE_URL = "https://xts-api.trading"
source = "WEBAPI"
xt = XTSConnect(API_KEY, API_SECRET, source)

response = xt.interactive_login()
# response = xt.marketdata_login()
print("Login: ", response)

orderList=xt.get_order_book()['result']
orderDf = pd.DataFrame(orderList)

tradeList=xt.get_trade()['result']
tradeDf = pd.DataFrame(tradeList)

positionList=xt.get_position_daywise()['result']['positionList']
posDf = pd.DataFrame(positionList)


placed_order = xt.place_order(exchangeSegment=xt.EXCHANGE_NSEFO,
                   exchangeInstrumentID=41379,
                   productType=xt.PRODUCT_MIS, 
                   orderType=xt.ORDER_TYPE_MARKET,                   
                   orderSide=xt.TRANSACTION_TYPE_SELL,
                   timeInForce=xt.VALIDITY_DAY,
                   disclosedQuantity=0,
                   orderQuantity=75,
                   limitPrice=0,
                   stopPrice=0,
                   orderUniqueIdentifier="dec29_2"
                   )
if placed_order['type'] != 'error':
         placed_orderID = placed_order['result']['AppOrderID']
         print("order id market order", placed_orderID)
placed_SL_order= xt.place_order(exchangeSegment=xt.EXCHANGE_NSEFO,
                   exchangeInstrumentID= 41379 ,
                   productType=xt.PRODUCT_MIS, 
                   orderType="StopMarket",                   
                   orderSide=xt.TRANSACTION_TYPE_BUY,
                   timeInForce=xt.VALIDITY_DAY,
                   disclosedQuantity=0,
                   orderQuantity=75,
                   limitPrice=0,
                   stopPrice=78.35+15,
                   orderUniqueIdentifier="dec29_sl_2"
                   )
if placed_SL_order['type'] != 'error':
         placed_SL_orderID = placed_SL_order['result']['AppOrderID']
         print("order id for StopLoss", placed_SL_orderID)

        
sq_off = xt.squareoff_position(
    exchangeSegment=xt.EXCHANGE_NSEFO,
    exchangeInstrumentID=39992,
    productType=xt.PRODUCT_MIS,
    squareoffMode=xt.SQUAREOFF_DAYWISE,
    positionSquareOffQuantityType=xt.SQUAREOFFQUANTITY_PERCENTAGE,
    squareOffQtyValue=100,
    blockOrderSending=True,
    cancelOrders=True)
print("Position Squareoff: ", sq_off)


orderList=xt.get_order_book()['result']
for i in orderList:
    # print(i)
    if i['OrderStatus'] == 'New':
        trgPen = i["AppOrderID"]
        print(trgPen)
        cancel_order = xt.cancel_order(
        appOrderID=trgPen,
        orderUniqueIdentifier='dec29_cancel_1')
        print("Cancel Order: ", cancel_order)

def get_global_PnL():
    # len(xt.get_position_daywise()['result']['positionList'])
    positionList=xt.get_position_daywise()['result']['positionList']
    totalMTM = 0.0
    for i in positionList:
        eachMTM = float(i['MTM'].replace(',', ''))
        #print(type(eachMTM))
        totalMTM += eachMTM
    print(totalMTM)
         


import time
start = time.time()
get_global_PnL()
print(f'Time: {time.time() - start}')

start = time.time()
get_global_PnL_df()
print(f'Time: {time.time() - start}')
    
from datetime import datetime
now = datetime.now()

import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
         
         
schedule.every(5).seconds.do(job)  
schedule.cancel_job(job)

import datetime

def dummy():
    return 1498

from datetime import datetime
import time

cdate = datetime.strftime(datetime.now(), "%d-%m-%Y")
check=True
m=0
bag=[]
while check:
    if (dummy() > 1500) or (datetime.now() >= datetime.strptime(cdate + " 23:00:00", "%d-%m-%Y %H:%M:%S")):
        print('trigger stop loss')
        check=False
    else:
        data = time.strftime("%d-%m-%Y %H:%M:%S"),",",dummy()
        # print(data)
        bag.append(data) 
        m+=1
        if len(bag) >= 5:
            tup=bag[-1]
            bagstr=" ".join(str(x) for x in tup)
            print(bagstr)
            bag = []
            m=0
        # print(m,len(bag))
        time.sleep(2)



type([data])

print(time.strftime("%d-%m-%Y %H:%M:%S"))
    
positionList= [{'AccountID': 'IIFL24', 'TradingSymbol': 'NIFTY 31DEC2020 CE 13900', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentId': '41376', 'ProductType': 'MIS', 'Marketlot': '75', 'Multiplier': '1', 'BuyAveragePrice': '0.00', 'SellAveragePrice': '82.70', 'OpenBuyQuantity': '0', 'OpenSellQuantity': '75', 'Quantity': '-75', 'BuyAmount': '0.00', 'SellAmount': '6,202.50', 'NetAmount': '6,202.50', 'UnrealizedMTM': '1,485.00', 'RealizedMTM': '0.00', 'MTM': '1,485.00', 'BEP': '82.70', 'SumOfTradedQuantityAndPriceBuy': '0.00', 'SumOfTradedQuantityAndPriceSell': '6,202.50', 'MessageCode': 9002, 'MessageVersion': 1, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227723717}, {'AccountID': 'IIFL24', 'TradingSymbol': 'NIFTY 31DEC2020 PE 13900', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentId': '41377', 'ProductType': 'MIS', 'Marketlot': '75', 'Multiplier': '1', 'BuyAveragePrice': '72.35', 'SellAveragePrice': '57.10', 'OpenBuyQuantity': '75', 'OpenSellQuantity': '75', 'Quantity': '0', 'BuyAmount': '5,426.25', 'SellAmount': '4,282.50', 'NetAmount': '-1,143.75', 'UnrealizedMTM': '0.00', 'RealizedMTM': '-1,143.75', 'MTM': '-1,143.75', 'BEP': '0.00', 'SumOfTradedQuantityAndPriceBuy': '5,426.25', 'SumOfTradedQuantityAndPriceSell': '4,282.50', 'MessageCode': 9002, 'MessageVersion': 1, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227723718}]

pos_df = pd.DataFrame(positionList)
for i in range(len(pos_df)):
    if int(pos_df["Quantity"].values[i]) != 0:
        symbol = pos_df["ExchangeInstrumentId"].values[i]
        print(symbol)
        
boo = int(pos_df["Quantity"].values[1])
a = pos_df["TradingSymbol"].values[0]
type(a)    
        

orderList = [{'LoginID': 'IIFL24', 'ClientID': 'IIFL24', 'AppOrderID': 20030623, 'OrderReferenceID': '', 'GeneratedBy': 'TWS', 'ExchangeOrderID': 'X_31475561', 'OrderCategoryType': 'NORMAL', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentID': 41376, 'OrderSide': 'Buy', 'OrderType': 'Market', 'ProductType': 'MIS', 'TimeInForce': 'DAY', 'OrderPrice': 0, 'OrderQuantity': 75, 'OrderStopPrice': 0, 'OrderStatus': 'New', 'OrderAverageTradedPrice': '88.45', 'LeavesQuantity': 0, 'CumulativeQuantity': 75, 'OrderDisclosedQuantity': 0, 'OrderGeneratedDateTime': '2020-12-30T13:50:53.7042412', 'ExchangeTransactTime': '2020-12-30T13:50:54+05:30', 'LastUpdateDateTime': '2020-12-30T13:50:54.0682695', 'OrderExpiryDate': '1980-01-01T00:00:00', 'CancelRejectReason': '', 'OrderUniqueIdentifier': '', 'OrderLegStatus': 'SingleOrderLeg', 'IsSpread': False, 'MessageCode': 9004, 'MessageVersion': 4, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227762024}, {'LoginID': 'IIFL24', 'ClientID': 'IIFL24', 'AppOrderID': 10025789, 'OrderReferenceID': '', 'GeneratedBy': 'TWSAPI', 'ExchangeOrderID': 'X_31475408', 'OrderCategoryType': 'NORMAL', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentID': 41377, 'OrderSide': 'Buy', 'OrderType': 'Market', 'ProductType': 'MIS', 'TimeInForce': 'DAY', 'OrderPrice': 0, 'OrderQuantity': 75, 'OrderStopPrice': 72.1, 'OrderStatus': 'Open', 'OrderAverageTradedPrice': '72.35', 'LeavesQuantity': 0, 'CumulativeQuantity': 75, 'OrderDisclosedQuantity': 0, 'OrderGeneratedDateTime': '2020-12-30T12:21:46.3067796', 'ExchangeTransactTime': '2020-12-30T12:39:39+05:30', 'LastUpdateDateTime': '2020-12-30T12:39:39.0228247', 'OrderExpiryDate': '1980-01-01T00:00:00', 'CancelRejectReason': '', 'OrderUniqueIdentifier': 'FirstChoice1', 'OrderLegStatus': 'SingleOrderLeg', 'IsSpread': False, 'MessageCode': 9004, 'MessageVersion': 4, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227762023}, {'LoginID': 'IIFL24', 'ClientID': 'IIFL24', 'AppOrderID': 10025788, 'OrderReferenceID': '', 'GeneratedBy': 'TWSAPI', 'ExchangeOrderID': 'X_31475407', 'OrderCategoryType': 'NORMAL', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentID': 41377, 'OrderSide': 'Sell', 'OrderType': 'Market', 'ProductType': 'MIS', 'TimeInForce': 'DAY', 'OrderPrice': 0, 'OrderQuantity': 75, 'OrderStopPrice': 0, 'OrderStatus': 'Filled', 'OrderAverageTradedPrice': '57.10', 'LeavesQuantity': 0, 'CumulativeQuantity': 75, 'OrderDisclosedQuantity': 0, 'OrderGeneratedDateTime': '2020-12-30T12:21:41.1823828', 'ExchangeTransactTime': '2020-12-30T12:21:41+05:30', 'LastUpdateDateTime': '2020-12-30T12:21:41.8754364', 'OrderExpiryDate': '1980-01-01T00:00:00', 'CancelRejectReason': '', 'OrderUniqueIdentifier': 'FirstChoice0', 'OrderLegStatus': 'SingleOrderLeg', 'IsSpread': False, 'MessageCode': 9004, 'MessageVersion': 4, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227762022}, {'LoginID': 'IIFL24', 'ClientID': 'IIFL24', 'AppOrderID': 10025787, 'OrderReferenceID': '', 'GeneratedBy': 'TWSAPI', 'ExchangeOrderID': 'X_31475406', 'OrderCategoryType': 'NORMAL', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentID': 41376, 'OrderSide': 'Buy', 'OrderType': 'StopMarket', 'ProductType': 'MIS', 'TimeInForce': 'DAY', 'OrderPrice': 0, 'OrderQuantity': 75, 'OrderStopPrice': 97.7, 'OrderStatus': 'New', 'OrderAverageTradedPrice': '', 'LeavesQuantity': 75, 'CumulativeQuantity': 0, 'OrderDisclosedQuantity': 0, 'OrderGeneratedDateTime': '2020-12-30T12:21:38.7891996', 'ExchangeTransactTime': '2020-12-30T12:21:38+05:30', 'LastUpdateDateTime': '2020-12-30T12:21:38.7901995', 'OrderExpiryDate': '1980-01-01T00:00:00', 'CancelRejectReason': '', 'OrderUniqueIdentifier': 'FirstChoice1', 'OrderLegStatus': 'SingleOrderLeg', 'IsSpread': False, 'MessageCode': 9004, 'MessageVersion': 4, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227762011}, {'LoginID': 'IIFL24', 'ClientID': 'IIFL24', 'AppOrderID': 10025786, 'OrderReferenceID': '', 'GeneratedBy': 'TWSAPI', 'ExchangeOrderID': 'X_31475405', 'OrderCategoryType': 'NORMAL', 'ExchangeSegment': 'NSEFO', 'ExchangeInstrumentID': 41376, 'OrderSide': 'Sell', 'OrderType': 'Market', 'ProductType': 'MIS', 'TimeInForce': 'DAY', 'OrderPrice': 0, 'OrderQuantity': 75, 'OrderStopPrice': 0, 'OrderStatus': 'Filled', 'OrderAverageTradedPrice': '82.70', 'LeavesQuantity': 0, 'CumulativeQuantity': 75, 'OrderDisclosedQuantity': 0, 'OrderGeneratedDateTime': '2020-12-30T12:21:33.377785', 'ExchangeTransactTime': '2020-12-30T12:21:33+05:30', 'LastUpdateDateTime': '2020-12-30T12:21:33.7418131', 'OrderExpiryDate': '1980-01-01T00:00:00', 'CancelRejectReason': '', 'OrderUniqueIdentifier': 'FirstChoice0', 'OrderLegStatus': 'SingleOrderLeg', 'IsSpread': False, 'MessageCode': 9004, 'MessageVersion': 4, 'TokenID': 0, 'ApplicationType': 0, 'SequenceNumber': 314802227762021}]
ord_df = pd.DataFrame(orderList)
pending = ord_df[ord_df['OrderStatus'].isin(["New","Open","Partially Filled"])]["AppOrderID"].tolist()

drop = []
attempt = 0
len(pending)

while len(pending)>0 and attempt<5:
    pending = [j for j in pending if j not in drop]
    for order in pending:
        try:
            print(order)
            drop.append(order)
            
        except:
            print("unable to print order id : ",order)
            attempt+=1


