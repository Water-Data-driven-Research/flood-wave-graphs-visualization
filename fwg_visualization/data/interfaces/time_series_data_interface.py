from dataclasses import dataclass

import pandas as pd


@dataclass
class TimeSeriesDataInterface:
    """
    Class for storing data preprocessed in a TimeSeriesDataHandler class.
    :param pd.DataFrame statistics: the statistics to be stored
    """
    statistics: pd.DataFrame = None
