from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.axis_data_calculator import AxisDataCalculator
from fwg_visualization.plot.data.edge_data_calculator import EdgeDataCalculator
from fwg_visualization.plot.data.interfaces.axis_data_interface import (
    AxisDataInterface
)
from fwg_visualization.plot.data.interfaces.edge_data_interface import (
    EdgeDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)
from fwg_visualization.plot.data.node_data_calculator import NodeDataCalculator


class FWGDataCreator:
    """
    This class creates the data necessary to plot a flood wave graph, and
    stores it in member variables.
    """
    def __init__(self, graph_data_if: GraphDataInterface):
        """
        Constructor
        :param GraphDataInterface graph_data_if: contains data about the graph
        """
        pass
