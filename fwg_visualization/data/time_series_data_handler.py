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

        self.data_if = TimeSeriesDataInterface()

    def run(self, year_range: dict):
        """
        Run function, preprocesses the data to make it easier to plot using
        plotly express, then stores it in a TimeSeriesDataInterface.
        :param dict year_range: the years for which to filter the data, the
               start and end years are both included in the filtered data
        """
        filtered_data = self.filter_data(data=self.data,
                                         year_range=year_range)

        self.data_if.statistics = filtered_data

    @staticmethod
    def filter_data(data: dict, year_range: dict) -> dict:
        """
        Filters the data for the given years.
        :param dict data: the data to be filtered (keys: station pairs,
               values: pandas DataFrames)
        :param dict year_range: the years for which to filter the data, the
               start and end years are both included in the filtered data
        :return dict: the filtered data
        """
        filtered_data: dict = {}

        for station_pair in data.keys():
            filtered_data[station_pair] = data[station_pair].loc[
                year_range['start']:year_range['end']
            ]

        return filtered_data
