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
                 rkm_station: dict):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        """
        self.graph_edges = graph_data_if.graph_edges
        self.positions = graph_data_if.positions
        self.rkm_station = rkm_station

        self.edge_data_if = EdgeDataInterface()

    def run(self):
        """
        Run function, calculates the required edge data and stores it in the
        EdgeDataInterface instance.
        """
        directed_edge_data = self.get_directed_edge_data()

        self.edge_data_if.directed_edge_data = directed_edge_data

    def get_directed_edge_data(self) -> list:
        """
        Calculates the positions of the directed edges.
        :return list: the positions of the directed edges
        """
        directed_edge_data: list = []

        for start, end in self.graph_edges:
            start_node_pos = self.positions[start]
            end_node_pos = self.positions[end]

            x_start = start_node_pos[0]
            x_end = end_node_pos[0]
            y_start = start_node_pos[1]
            y_end = end_node_pos[1]

            dx = x_end - x_start
            dy = y_end - y_start

            edge_data_dict = {
                'x_start': round(x_start + dx / 80, 6),
                'y_start': round(y_start + dy / 80, 6),
                'x_end': round(x_end - dx / 15, 6),
                'y_end': round(y_end - dy / 15, 6)
            }

            directed_edge_data.append(edge_data_dict)

        return directed_edge_data
