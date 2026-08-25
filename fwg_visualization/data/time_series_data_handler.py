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
        Run function, filters the data for the given years, then stores it in
        the TimeSeriesDataInterface instance.
        :param dict year_range: the years for which to filter the data, the
               start and end years are both included in the filtered data
        """
        self.data_if.statistics = {}

        for station_pair in self.data.keys():
            self.data_if.statistics[station_pair] = (
                self.data[station_pair].loc[
                    year_range['start']:year_range['end']
                ]
            )
