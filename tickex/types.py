from dataclasses import dataclass, asdict


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

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)
