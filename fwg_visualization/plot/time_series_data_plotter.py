import plotly.graph_objects as go

from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)


class TimeSeriesDataPlotter:
    """
    This class creates the plot of the received time series data.
    """
    def __init__(self, data_if: TimeSeriesDataInterface):
        """
        Constructor.
        :param TimeSeriesDataInterface data_if: contains data to be plotted
        """
        self.statistics = data_if.statistics

    def plot_ts_data(self,
                     statistic: str,
                     unit_of_measurement: str,
                     rkm_station: dict,
                     width: int = 1000,
                     height: int = 500):
        """
        Creates the plot of the received data.
        :param str statistic: the statistic that we are plotting, one of the
               following: 'flood wave count', 'mean propagation time',
               'median propagation time', 'mode propagation time'
        :param str unit_of_measurement: the unit of measurement used on the
               y-axis
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        :raise ValueError: if the period frequency of the pandas DataFrames
               is unsupported
        """
        fig = go.Figure()

        df_test = list(self.statistics.values())[0]
        if df_test.index.freq == 'YE':
            graph_name = f'Yearly {statistic}'
        elif df_test.index.freq == 'QE':
            graph_name = f'Quarterly {statistic}'
        else:
            raise ValueError(
                f'Unsupported period frequency: {df_test.index.freq}'
            )

        for pair, df in self.statistics.items():
            fig.add_trace(trace=go.Scatter(
                x=df.index.astype(str).tolist(),
                y=df[statistic],
                mode='lines',
                name=f'{rkm_station[pair[0]]}---{rkm_station[pair[1]]}'
            ))

        self.create_layout(fig=fig,
                           graph_name=graph_name,
                           unit_of_measurement=unit_of_measurement,
                           width=width,
                           height=height)
        fig.show()

    @staticmethod
    def create_layout(fig: go.Figure,
                      graph_name: str,
                      unit_of_measurement: str,
                      width: int,
                      height: int):
        """
        Creates the layout of the received figure.
        :param go.Figure fig: the figure to customize
        :param str graph_name: what the name of the graph should be
        :param str unit_of_measurement: the unit of measurement used on the
               y-axis
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        """
        fig.update_layout(
            title={
                'text': graph_name,
                'xanchor': 'center',
                'yanchor': 'top',
                'x': 0.5,
                'y': 0.98
            },
            width=width,
            height=height,
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis={
                'title': dict(text='Date'),
                'tickmode': 'linear'
            },
            yaxis=dict(title=dict(text=unit_of_measurement)),
            legend=dict(title=dict(text='Station pairs')),
            hovermode='x unified'
        )
