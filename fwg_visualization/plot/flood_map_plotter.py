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
                               height: int = 500) -> go.Figure:
            """
            Creates the plot of the flood map.
            :param str graph_name: 'Flood Map' by default
            :param int width: the width of the image to be created (pixels)
            :param int height: the height of the image to be created (pixels)
            :return go.Figure: the created plot
            """
            fig = self.get_fwg_plot(graph_name=graph_name,
                                    width=width,
                                    height=height)

            boundary_stations = list(set(self.node_data_if.y_coordinates))
            for station in boundary_stations:
                fig.add_hline(y=station, line_color='red')

            return fig

    return FloodMapPlotter
