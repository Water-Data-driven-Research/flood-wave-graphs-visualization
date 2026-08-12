from datetime import timedelta

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.axis_data_interface import (
    AxisDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)


class AxisDataCalculator:
    """
    Calculates the data to be put on the x- and y-axes that will be displayed
    on the figure.
    """
    def __init__(self,
                 graph_if: GraphDataInterface,
                 node_if: NodeDataInterface):
        """
        Constructor.
        """
        pass
