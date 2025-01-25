from dataclasses import dataclass, asdict
import datetime


@dataclass
class Ticker:
    """Ticker object for market ticker data"""
    name: str
    timestamp: str | datetime.datetime
    close: float
    high: float
    low: float
    open: float
    volume: float
    interval: str

    def to_dict(self, dt_enabled=False) -> dict:
        """Create to a dict from the Ticker.

        If `dt_enabled` is True, translate the timestamp to a datetime object.

        :return dict:
        """
        dictionary = asdict(self)
        if dt_enabled and isinstance(dictionary['timestamp'], str):
            dictionary['timestamp'] = datetime.datetime.fromisoformat(
                dictionary['timestamp']
            )
        elif not dt_enabled and isinstance(
                dictionary['timestamp'],
                datetime.datetime):
            dictionary['timestamp'] = dictionary['timestamp'].isoformat()
        return dictionary

    @classmethod
    def from_dict(cls, dictionary, dt_enabled=False) -> 'Ticker':
        """Create a Ticker from a dict

        :return Ticker:
        """
        if not dt_enabled and isinstance(
                dictionary['timestamp'],
                datetime.datetime):
            dictionary['timestamp'] = dictionary['timestamp'].isoformat()
        elif dt_enabled and isinstance(dictionary['timestamp'], str):
            dictionary['timestamp'] = datetime.datetime.fromisoformat(
                dictionary['timestamp']
            )
        # ignore extraneous args
        return cls(**{
            k: v for k, v in dictionary.items()
            if k in cls.__annotations__.keys()
        })
