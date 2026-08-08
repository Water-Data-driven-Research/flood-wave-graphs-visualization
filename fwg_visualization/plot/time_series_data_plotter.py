import plotly

from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)


class TimeSeriesDataPlotter:
    """
    This class creates the plot of the received time series data.
    """
    def __init__(self, ts_data_if: TimeSeriesDataInterface):
        """
        Constructor.
        :param TimeSeriesDataInterface ts_data_if: contains data to be plotted
        """
        self.statistics = ts_data_if.statistics
