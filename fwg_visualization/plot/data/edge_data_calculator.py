from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.edge_data_interface import (
    EdgeDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)


class EdgeDataCalculator:
    """
    Calculates the data required to make the edges of the directed graph,
    as well as data required to make very small markers (edge hover trace)
    to implement the hover functionality on edges.
    """
    def __init__(self,
                 graph_data_if: GraphDataInterface,
                 node_data_if: NodeDataInterface):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param NodeDataInterface node_data_if: contains data about the nodes
        """
        pass

    def run(self):
        """
        Run function, calculates the required edge data and instantiates an
        EdgeDataInterface to store it.
        """
        pass

    def get_edge_data(self):
        """
        Calculates the positions of the directed edges and the positions of
        the small markers used to create hover functionality for the edges,
        and the data required to make the hover text of the edges.
        :return dict: the data we need about the edges
        """
        pass
