import pandas as pd

from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)


class TimeSeriesDataHandler:
    """
    This class preprocesses the received yearly and quarterly statistics for
    visualization.
    """
    def __init__(self, data: dict):
        """
        Constructor.
        :param dict data: the data to be preprocessed (the statistics),
               keys: station pairs, values: pandas DataFrames (data of the
               given station pairs)
        """
        self.data = data

        self.time_series_data_interface = TimeSeriesDataInterface()

    def run(self):
        """
        Run function, preprocesses the data to make it easier to plot using
        plotly express, then stores it in a TimeSeriesDataInterface.
        """
        combined_data_frame = pd.concat(
            objs=self.data,
            names=['station_pair']
        ).reset_index()

        self.time_series_data_interface = TimeSeriesDataInterface(
            statistics=combined_data_frame
        )
