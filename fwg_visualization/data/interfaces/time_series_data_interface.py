from dataclasses import dataclass


@dataclass
class TimeSeriesDataInterface:
    """
    Class for storing data preprocessed in a TimeSeriesDataHandler class.
    :param dict statistics: the statistics to be stored
    """
    statistics: dict = None
