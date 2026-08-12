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
                 graph_if: GraphDataInterface,
                 edge_if: EdgeDataInterface):
        """
        Constructor.
        """
        pass