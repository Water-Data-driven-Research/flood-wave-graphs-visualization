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

    def run(self, year_range: dict):
        """
        Run function, preprocesses the data to make it easier to plot using
        plotly express, then stores it in a TimeSeriesDataInterface.
        :param dict year_range: the years for which to filter the data, the
               start and end years are both included in the filtered data
        """
        self.filter_data(year_range=year_range)

        self.time_series_data_interface = TimeSeriesDataInterface(
            statistics=self.data
        )

    def filter_data(self, year_range: dict):
        """
        Filters the data for the given years.
        :param dict year_range: the years for which to filter the data, the
               start and end years are both included in the filtered data
        :return pd.DataFrame: the filtered data
        """
        for station_pair in self.data.keys():
            self.data[station_pair] = self.data[station_pair].loc[
                year_range['start']:year_range['end']
            ]
