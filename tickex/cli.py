import yfinance as yf
import datetime as dt

def main():
    print("tickex main")
    start_date = dt.datetime.today()- dt.timedelta(1000) 
    end_date = dt.datetime.today()
    stock ="USDJPY=X"
    data = yf.download(stock, start_date, end_date)
    print(data)