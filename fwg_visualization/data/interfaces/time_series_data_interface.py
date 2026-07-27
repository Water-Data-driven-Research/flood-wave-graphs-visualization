from dataclasses import dataclass
import pandas as pd


@dataclass
class TimeSeriesDataInterface:
    """
    Class for storing data preprocessed in a TimeSeriesDataHandler class.
    """
    def __init__(self, statistics: pd.DataFrame = None):
        pass
