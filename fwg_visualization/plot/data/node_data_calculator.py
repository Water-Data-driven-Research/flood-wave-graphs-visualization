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
                 graph_data_if: GraphDataInterface,
                 rkm_station: dict,
                 level_group: dict):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        :param dict level_group: the dictionary that maps station positions on
               the river to their level groups (values above which a water
               level is considered high)
        """
        pass
