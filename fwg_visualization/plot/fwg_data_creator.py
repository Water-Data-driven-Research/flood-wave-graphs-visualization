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
    def __init__(self,
                 graph_data_if: GraphDataInterface,
                 rkm_station: dict,
                 vertex_data: dict,
                 level_group: dict):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        :param dict vertex_data: data about the delta peaks, structure:
               {station1: {date1: {'value': value1, 'color': color1},
                           date2: {'value': value2, 'color': color2},
                           ...},
                station2: {date1: {'value': value1, 'color': color1},
                           date2: {'value': value2, 'color': color2},
                           ...},
                ...}
        :param dict level_group: the dictionary that maps station positions on
               the river to their level groups (values above which a water
               level is considered high)
        """
        self.graph_data_if = graph_data_if
        self.rkm_station = rkm_station
        self.vertex_data = vertex_data
        self.level_group = level_group

        self.node_data_if = NodeDataInterface()
        self.axis_data_if = AxisDataInterface()
        self.edge_data_if = EdgeDataInterface()

    def run(self):
        """
        Run function, fills the node, axis, and edge data interfaces.
        """
        self.calculate_node_data()
        self.calculate_axis_data()
        self.calculate_edge_data()

    def calculate_node_data(self):
        """
        Instantiates a NodeDataCalculator to calculate the required node data.
        """
        node_data_calculator = NodeDataCalculator(
            graph_data_if=self.graph_data_if,
            rkm_station=self.rkm_station,
            vertex_data=self.vertex_data,
            level_group=self.level_group
        )
        node_data_calculator.run()
        self.node_data_if = node_data_calculator.node_data_if

    def calculate_axis_data(self):
        """
        Instantiates an AxisDataCalculator to calculate the required axis data.
        """
        axis_data_calculator = AxisDataCalculator(
            graph_data_if=self.graph_data_if
        )
        axis_data_calculator.run()
        self.axis_data_if = axis_data_calculator.axis_data_if

    def calculate_edge_data(self):
        """
        Instantiates an EdgeDataCalculator to calculate the required edge data.
        """
        edge_data_calculator = EdgeDataCalculator(
            graph_data_if=self.graph_data_if,
            rkm_station=self.rkm_station
        )
        edge_data_calculator.run()
        self.edge_data_if = edge_data_calculator.edge_data_if
