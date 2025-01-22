import logging
import datetime


logger = logging.getLogger(__name__)


class Pipeline:
    """ETL Pipeline class"""
    def __init__(self, extractor, translator, loader):
        self.extractor = extractor
        self.translator = translator
        self.loader = loader

    def get_start_date(self, interval: str):
        if interval == '1d':
            # Get everything you can from 5 years ago daily interval
            delta = datetime.timedelta(days=365*5)
        elif interval == '15m':
             # Get everything you can from 60 days ago 15m interval
            delta = datetime.timedelta(days=59)
        else:
            raise ValueError("Only '1d' and '15m' supported for interval")
        today = datetime.datetime.today()
        return today - delta
    
    def run(self, intervals: list = ['1d', '15m']):
        """Run the ETL pipeline

        :return None:
        """
        for interval in intervals:
            df = self.extractor.extract(
                start_date=self.get_start_date(interval),
                end_date=datetime.datetime.today(),
                interval=interval
            )
            tickers = self.translator.translate(df, interval)
            self.loader.load(tickers, interval)
