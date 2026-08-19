from typing import Type

import plotly.graph_objects as go


def flood_map_plotter(cls: Type) -> Type:
    """
    Acts as a decorator to add flood map plotting functionality.
    :param Type cls: the FWGPlotter to which we add a new method
    :return Type: the updated FWGPlotter
    """
    class FloodMapPlotter(cls):
        """
        This class adds flood map plotting functionality to an FWGPlotter.
        """
        def get_flood_map_plot(self,
                               graph_name: str = 'Flood Map',
                               width: int = 1000,
                               height: int = 500,
                               boundary_stations: list = None) -> go.Figure:
            """
            Creates the plot of the flood map.
            :param str graph_name: 'Flood Map' by default
            :param int width: the width of the image to be created (pixels)
            :param int height: the height of the image to be created (pixels)
            :param list boundary_stations: the stations on the boundaries of
                   river sections
            :return go.Figure: the created plot
            """
            if boundary_stations is None:
                boundary_stations = []

            fig = self.get_fwg_plot(graph_name=graph_name,
                                    width=width,
                                    height=height)

            yaxis = fig.layout.yaxis
            station_y_mapping: dict = {s: c for s, c in
                                       zip(yaxis.ticktext, yaxis.tickvals)}

            x_range: tuple = fig.layout.xaxis.range
            for station in list(range(len(boundary_stations))):
                y_coord = station_y_mapping[station]
                line = go.Scatter(
                    x=[x_range[0], x_range[1]],
                    y=[y_coord, y_coord],
                    mode='lines',
                    line={
                        'color': 'black',
                        'width': 1
                    },
                    hoverinfo='skip'
                )
                fig.add_trace(line)

            traces = list(fig.data)
            line_number = len(boundary_stations)
            other_traces = traces[:-line_number]
            line_traces = traces[-line_number:]

            fig.data = tuple(line_traces + other_traces)

            return fig

    return FloodMapPlotter
