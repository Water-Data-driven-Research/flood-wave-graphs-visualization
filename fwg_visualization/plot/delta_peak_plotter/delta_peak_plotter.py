from datetime import datetime, timedelta

import pandas as pd
import plotly.colors as colors
import plotly.graph_objects as go

from fwg_visualization.plot.delta_peak_plotter.interfaces. \
    delta_peak_data_interface import DeltaPeakDataInterface


class DeltaPeakPlotter:
    """
    This class creates a plot showcasing what a delta peak is.
    """
    def __init__(self, delta_peak_data_interface: DeltaPeakDataInterface):
        """
        Constructor.
        :param DeltaPeakDataInterface delta_peak_data_interface: contains the
               delta peaks and the water levels to be plotted
        """
        self.delta_peaks: pd.Series = delta_peak_data_interface.delta_peaks
        self.data_points: pd.Series = delta_peak_data_interface.data_points
        self.delta: int = delta_peak_data_interface.delta

    def create_plot(self,
                    graph_name: str,
                    width: int = 1400,
                    height: int = 600) -> go.Figure:
        """
        Creates the plot of the water levels and delta peaks.
        :param str graph_name: the name of the graph
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        :return go.Figure: the created plot
        """
        fig = go.Figure()

        self.create_data_trace(fig=fig)
        self.create_delta_trace(fig=fig)

        self.create_lines(fig=fig)
        self.create_layout(fig=fig,
                           graph_name=graph_name,
                           width=width,
                           height=height)

        return fig

    def create_data_trace(self, fig: go.Figure):
        """
        Creates and adds the trace that includes the water levels at each date.
        :param go.Figure fig: the figure we are creating
        """
        data_trace = go.Scatter(
            x=self.data_points.index,
            y=self.data_points,
            customdata=list(zip(self.data_points.index.astype(dtype=str),
                                self.data_points)),
            hovertemplate=('<b>%{customdata[0]}</b><br>'
                           'Water level: %{customdata[1]} m<extra></extra>'),
            mode='markers+lines',
            marker=dict(color='lightblue',
                        size=12,
                        line_width=1)
        )

        fig.add_trace(trace=data_trace)

    def create_delta_trace(self, fig: go.Figure):
        """
        Creates and adds the trace that includes the delta peak markers.
        :param go.Figure fig: the figure we are creating
        """
        delta_trace = go.Scatter(
            x=self.delta_peaks.index,
            y=self.delta_peaks,
            customdata=list(zip(self.delta_peaks.index.astype(dtype=str),
                                self.delta_peaks)),
            hovertemplate=('<b>%{customdata[0]}</b><br>'
                           'Water level: %{customdata[1]} m<extra></extra>'),
            mode='markers',
            marker=dict(color=colors.qualitative.Plotly,
                        size=12,
                        line_width=1)
        )

        fig.add_trace(trace=delta_trace)

    def create_lines(self, fig: go.Figure):
        """
        Adds the vertical lines to indicate how far the delta range applies
        around a delta peak.
        :param go.Figure fig: the figure to add lines to
        """
        dates = self.delta_peaks.index

        for i in range(len(dates)):
            current_date = datetime.strptime(dates[i], '%Y-%m-%d')
            fig.add_vline(x=current_date - timedelta(days=self.delta),
                          layer='above',
                          line_color=(
                              fig.data[1].marker.color[i]
                              if i < len(fig.data[1].marker.color)
                              else 'black'
                          ),
                          line_dash='dash',
                          line_width=2.5)
            fig.add_vline(x=current_date + timedelta(days=self.delta),
                          layer='above',
                          line_color=(
                              fig.data[1].marker.color[i]
                              if i < len(fig.data[1].marker.color)
                              else 'black'
                          ),
                          line_dash='dash',
                          line_width=2.5)

    @staticmethod
    def create_layout(fig: go.Figure,
                      graph_name: str,
                      width: int = 1400,
                      height: int = 600):
        """
        Creates and adds the layout to the received figure.
        :param go.Figure fig: updates the layout of this figure
        :param str graph_name: the name of the graph
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
            showlegend=False,
            hovermode='closest',
            margin=dict(b=30, l=30, r=30, t=40),
            xaxis={
                'title': dict(text='Dátum'),
                'dtick': 'D1'
            },
            yaxis={
                'title': dict(text='Abszolút változás'),
                'dtick': 0.1
            },
            width=width,
            height=height
        )
