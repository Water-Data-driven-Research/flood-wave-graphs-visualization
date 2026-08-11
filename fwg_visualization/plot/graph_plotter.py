import plotly.graph_objects as go

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class GraphPlotter:
    """
    This class creates the plot of the received flood wave graph or flood map.
    """
    def __init__(self, graph_data_interface: GraphDataInterface):
        """
        Constructor.
        :param GraphDataInterface graph_data_interface: contains data for
               plotting
        """
        pass

    def get_graph_plot(self,
                       graph_name: str = 'Flood Wave Graph',
                       width: int = 1000,
                       height: int = 500) -> go.Figure:
        """
        Creates the plot of the graph.
        :param str graph_name: 'Flood Wave Graph' or 'Flood Map'
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        :return go.Figure:
        """
        pass

    def create_node_trace(self, node_data: dict) -> go.Scatter:
        """
        Creates the trace that includes the nodes of the graph.
        :return go.Scatter: the trace of the nodes
        """
        pass

    def create_edge_hover_trace(self) -> go.Scatter:
        """
        Creates the trace that includes the invisible markers that simulate
        the hover function for the edges.
        :return go.Scatter: the miniscule markers in the middle of the edges
        """
        pass

    @staticmethod
    def create_layout(fig: go.Figure,
                      axis_data: dict,
                      graph_name: str,
                      width: int,
                      height: int):
        """
        Creates the layout of the received figure.
        :param go.Figure fig: updates the layout of this figure
        :param dict axis_data: the data to display on the axes of the figure
        :param str graph_name: the name of the graph ('Flood Wave Graph' or
               'Flood Map')
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        """
        pass
