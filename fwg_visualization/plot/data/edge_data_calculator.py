from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.edge_data_interface import (
    EdgeDataInterface
)


class EdgeDataCalculator:
    """
    Calculates the data required to make the edges of the directed graph.
    """
    def __init__(self, graph_data_if: GraphDataInterface):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        """
        self.graph_edges = graph_data_if.graph_edges
        self.positions = graph_data_if.positions

        self.data_if = EdgeDataInterface()

    def run(self):
        """
        Run function, calculates a list of the positions of the directed edges
        and stores it in the EdgeDataInterface instance.
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

        self.data_if.directed_edge_data = directed_edge_data
