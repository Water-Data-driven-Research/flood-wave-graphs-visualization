import plotly.graph_objects as go

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

    def plot_ts_data(self,
                     statistic: str,
                     graph_name: str,
                     unit_of_measure: str,
                     rkm_station: dict):
        """
        Creates the plot of the received data.
        :param str statistic: the statistic that we are plotting, one of the
               following: 'flood wave count', 'mean propagation time',
               'median propagation time', 'mode propagation time'
        :param str graph_name: what the name of the graph should be
        :param str unit_of_measure: the unit of measurement used on the y-axis
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        """
        fig = go.Figure()
        for pair, df in self.statistics.items():
            fig.add_trace(trace=go.Scatter(
                x=df.index,
                y=df[statistic],
                mode='lines',
                name=f'{rkm_station[pair[0]]}---{rkm_station[pair[1]]}'
            ))

        self.create_layout(fig=fig,
                           graph_name=graph_name,
                           unit_of_measure=unit_of_measure)
        fig.show()

    @staticmethod
    def create_layout(fig: go.Figure, graph_name: str, unit_of_measure: str):
        """
        Creates the layout of the received figure.
        :param go.Figure fig: the figure to customize
        :param str graph_name: what the name of the graph should be
        :param str unit_of_measure: the unit of measurement used on the y-axis
        """
        pass
