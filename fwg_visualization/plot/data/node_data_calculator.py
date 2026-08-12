from datetime import datetime

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)


class NodeDataCalculator:
    """
    Calculates the data required to make the node markers (node trace).
    """
    def __init__(self,
                 graph_if: GraphDataInterface,
                 rkm_station: dict,
                 level_group: dict):
        """
        Constructor.
        :param GraphDataInterfcae
        """
        pass
