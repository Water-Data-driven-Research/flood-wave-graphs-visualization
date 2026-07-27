import networkx as nx
import plotly

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
