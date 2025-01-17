import datetime
from tickex import data
import json


def main():
    today = datetime.datetime.today()
    # Get everything you can from 5 years ago daily interval
    years_start_1d_interval = datetime.timedelta(days=1) #(days=365*5) 
    # Get everything you can from 60 days ago 15m interval
    days_start_15m_interval = datetime.timedelta(days=1)#(days=60)
    
    day_tickers = data.get_tickers(
        start_date=today - years_start_1d_interval,
        end_date=today,
        interval='1d'
    )
    for t in day_tickers:
        filename = f"{t.name}_{t.interval}_{t.timestamp}.json"
        with open(filename, 'w') as jf:
            json.dump(t.to_dict(), jf, indent=2)

    intraday_tickers = data.get_tickers(
        start_date=today - days_start_15m_interval,
        end_date=today,
        interval='15m'
    )

    for t in intraday_tickers:
        filename = f"{t.name}_{t.interval}_{t.timestamp}.json"
        with open(filename, 'w') as jf:
            json.dump(t.to_dict(), jf, indent=2)
