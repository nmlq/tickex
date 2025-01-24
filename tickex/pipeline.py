import logging
import datetime


logger = logging.getLogger(__name__)


class Pipeline:
    """ETL Pipeline class"""
    def __init__(
            self, 
            extractor,
            translator,
            loader,
            supported_intervals: set = {'1d' ,'15m'}):
        self.extractor = extractor
        self.translator = translator
        self.loader = loader
        self.supported_intervals = supported_intervals

    def utcnow(self) -> datetime.datetime:
        """Get datetime now object by UTC offset
        
        :return datetime:
        """
        return datetime.datetime.utcnow()

    def get_start_date(
            self,
            interval: str) -> datetime.datetime:
        """Get the start date.

        Read the most recent start date from the loader if available.

        :return datetime:
        """
        # If collection exists, get the last timestamp and update
        current = self.utcnow()
        if interval in self.loader.database.list_collection_names():
            logger.info(f"Getting latest tickers for interval {interval}")
            collection = self.loader.get_collection(interval)
            last_one = collection.find_one({}, {"timestamp": -1})
            past = last_one['timestamp']
            logger.info(f"Last timestamp {last_one['timestamp'].isoformat()}")
            logger.info(f"Current timestamp {current.isoformat()}")
            return current - (current - past)

        # No collection for this interval exists, populate it.
        logger.info(f"Populating new collection interval with data {interval}")
        if interval == '1d':
            # Get everything you can from 5 years ago daily interval
            delta = datetime.timedelta(days=365*5)
        elif interval == '15m':
             # Get everything you can from 60 days ago 15m interval
            delta = datetime.timedelta(days=59)
            
        return current - delta
    
    def run(self):
        """Run the ETL pipeline

        :return None:
        """
        for interval in self.supported_intervals:
            df = self.extractor.extract(
                start_date=self.get_start_date(interval),
                end_date=self.utcnow(),
                interval=interval
            )

            if df.empty:
                logger.info(f"No ticker data extracted, skipping interval {interval}")
                continue
            
            tickers = self.translator.translate(df, interval)
            self.loader.load(tickers, interval)
