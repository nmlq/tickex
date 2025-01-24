from dataclasses import dataclass, asdict
import datetime


@dataclass
class Ticker:
    """Ticker object for market ticker data"""
    name: str
    timestamp: str
    close: float
    high: float
    low: float
    open: float
    volume: float
    interval: str

    def to_dict(self, dt_enabled = False) -> dict:
        """Create to a dict from the Ticker.

        If `dt_enabled` is True, translate the timestamp to a datetime object.

        :return dict:
        """
        dictionary = asdict(self)
        if dt_enabled:
            dictionary['timestamp'] = datetime.datetime.fromisoformat(
                dictionary['timestamp']
            )
        return dictionary

    @classmethod
    def from_dict(cls, dictionary) -> 'Ticker':
        """Create a Ticker from a dict

        :return Ticker:
        """
        if isinstance(dictionary['timestamp'], datetime.datetime):
            dictionary['timestamp'] = dictionary['timestamp'].isoformat()
        return cls(**dictionary)
