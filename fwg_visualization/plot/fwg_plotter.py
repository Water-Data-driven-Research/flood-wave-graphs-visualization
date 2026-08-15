import plotly.graph_objects as go

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class FWGPlotter:
    """
    This class creates the plot of the received flood wave graph.
    """
    def __init__(self, graph_data_interface: GraphDataInterface):
        """
        Constructor.
        :param GraphDataInterface graph_data_interface: contains data for
               plotting
        """
        pass

    def get_graph_plot(self,
                       width: int = 1000,
                       height: int = 500,
                       graph_name: str = 'Flood Wave Graph') -> go.Figure:
        """
        Creates the plot of the graph.
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        :param str graph_name: 'Flood Wave Graph' by default
        :return go.Figure: the created plot
        """
        pass

    def create_node_trace(self) -> go.Scatter:
        """
        Creates the trace that includes the nodes of the graph.
        :return go.Scatter: the trace of the nodes
        """
        pass

    def create_edge_hover_trace(self) -> go.Scatter:
        """
        Creates the trace that includes the miniscule markers that enable
        hover functionality for the edges.
        :return go.Scatter: the trace of the edge markers
        """
        pass

    def create_directed_edges(self) -> list:
        """
        Creates the arrows that are the directed edges of the graph.
        :return list: a list of arrows (each represented as a dictionary)
        """
        pass

    def create_layout(self,
                      fig: go.Figure,
                      graph_name: str,
                      width: int,
                      height: int):
        """
        Creates the layout of the received figure.
        :param go.Figure fig: updates the layout of this figure
        :param str graph_name: the name of the graph ('Flood Wave Graph' by
               default)
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        """
        pass
