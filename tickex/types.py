from dataclasses import dataclass, asdict
import datetime


@dataclass
class Ticker:
    name: str
    timestamp: str
    close: float
    high: float
    low: float
    open: float
    volume: float
    interval: str

    def to_dict(self, dt_enabled = False):
        dictionary = asdict(self)
        if dt_enabled:
            dictionary['timestamp'] = datetime.datetime.fromisoformat(
                dictionary['timestamp']
            )
        return dictionary

    @classmethod
    def from_dict(cls, dictionary):
        if isinstance(dictionary['timestamp'], datetime.datetime):
            dictionary['timestamp'] = dictionary['timestamp'].isoformat()
        return cls(**dictionary)
