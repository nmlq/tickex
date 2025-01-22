import datetime
from tickex import data
from tickex import database
import logging
import tqdm


logger = logging.getLogger(__name__)


def main():
    logger.info("Starting main cli")
    today = datetime.datetime.today()

    logger.info("Gathering 5 years of 1d data")
    # Get everything you can from 5 years ago daily interval
    years_start_1d_interval = datetime.timedelta(days=365*5)

    logger.info("Gathering 60 days of 15m data")
    # Get everything you can from 60 days ago 15m interval
    days_start_15m_interval = datetime.timedelta(days=59)

    logger.info("getting the 1d collection")
    collection_1d = database.get_collection('1d')
    day_tickers = data.get_tickers(
        start_date=today - years_start_1d_interval,
        end_date=today,
        interval='1d'
    )
    logger.info("Inserting 1d ticker data")
    data_1d = []
    for t in tqdm.tqdm(day_tickers):
        d = t.to_dict()
        d['timestamp'] = datetime.datetime.fromisoformat(d['timestamp'])
        data_1d.append(d)
    collection_1d.insert_many(data_1d)

    logger.info("getting the 15m collection")
    collection_1d = database.get_collection('15m')
    intraday_tickers = data.get_tickers(
        start_date=today - days_start_15m_interval,
        end_date=today,
        interval='15m'
    )
    logger.info("Inserting 1d ticker data")
    data_15m = []
    for t in tqdm.tqdm(intraday_tickers):
        d = t.to_dict()
        d['timestamp'] = datetime.datetime.fromisoformat(d['timestamp'])
        data_15m.append(d)
    collection_1d.insert_many(data_15m)

    logger.info("Completed inserts")
