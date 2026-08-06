import pandas as pd

from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)


class TimeSeriesDataHandler:
    """
    This class preprocesses the received yearly and quarterly statistics for
    visualization.
    """
    def __init__(self, year_range: tuple, data: dict):
        """
        Constructor.
        :param dict data: the data to be preprocessed (the statistics),
               keys: station pairs, values: pandas DataFrames (data of the
               given station pairs)
        """
        self.data = data
        self.year_range = year_range

        self.time_series_data_interface = TimeSeriesDataInterface()

    def run(self):
        """
        Run function, preprocesses the data to make it easier to plot using
        plotly express, then stores it in a TimeSeriesDataInterface.
        """
        self.filter_data()

        self.time_series_data_interface = TimeSeriesDataInterface(
            statistics=self.data
        )

    def filter_data(self):
        """
        Filters the data for the given years.
        :return pd.DataFrame: the filtered data
        """
        for station_pair in self.data.keys():
            self.data[station_pair] = self.data[station_pair].loc[
                self.year_range[0]:self.year_range[1]
            ]
