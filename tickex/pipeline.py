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
            supported_intervals: set = {'1d', '15m'}):
        self.extractor = extractor
        self.translator = translator
        self.loader = loader
        self.supported_intervals = supported_intervals

    def get_start_date(
            self,
            interval: str) -> datetime.datetime:
        """Get the start date.

        Read the most recent start date from the loader if available.

        :return datetime:
        """
        # If collection exists, get the last timestamp and update
        current = datetime.datetime.utcnow()
        logger.info(f"Current timestamp {current.isoformat()}")
        last_ticker = self.loader.get_last_ticker(interval)

        logger.info(f"Populating new collection interval with data {interval}")
        if last_ticker is not None:
            logger.info(f"Last timestamp {last_ticker.timestamp.isoformat()}")
            delta = (current - last_ticker.timestamp)
        # No collection for the following intervals; populate.
        elif interval == '1d' and last_ticker is None:
            # Get everything you can from 5 years ago daily interval
            delta = datetime.timedelta(days=365*5)
        elif interval == '15m' and last_ticker is None:
            # Get everything you can from 60 days ago 15m interval
            delta = datetime.timedelta(days=59)
        else:
            # We should never get here, but let's throw and exception
            # because we should always define a `delta` and there is no
            # sensible default `delta` to choose
            raise Exception(
                "Unknown interval, timestamp error, or other data error"
            )

        return current - delta

    def run(self) -> 'Pipeline':
        """Run the ETL pipeline

        :return self:
        """
        for interval in self.supported_intervals:
            df = self.extractor.extract(
                start_date=self.get_start_date(interval),
                end_date=datetime.datetime.utcnow(),
                interval=interval
            )

            if df.empty:
                logger.info(
                    f"No ticker data extracted, skipping interval {interval}"
                )
                continue

            tickers = self.translator.translate(df, interval)
            self.loader.load(tickers, interval)
        return self
