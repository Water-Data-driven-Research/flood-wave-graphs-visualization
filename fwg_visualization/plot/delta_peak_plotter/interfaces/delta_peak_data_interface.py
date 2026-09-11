from dataclasses import dataclass

import pandas as pd


@dataclass
class DeltaPeakDataInterface:
    """
    Class for storing data created in a DeltaPeakDataHandler.
    :param pd.Series delta_peaks: the delta peaks for every date
    :param pd.Series data_points: the water levels for every date
    :param int delta: the delta value we are visualizing
    """
    delta_peaks: pd.Series = None
    data_points: pd.Series = None
    delta: int = None
