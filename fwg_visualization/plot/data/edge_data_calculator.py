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
                 node_data_if: NodeDataInterface,
                 rkm_station: dict):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param NodeDataInterface node_data_if: contains data about the nodes
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        """
        self.graph_edges = graph_data_if.graph_edges
        self.positions = node_data_if.positions
        self.rkm_station = rkm_station

        self.edge_data_if = EdgeDataInterface()

    def run(self):
        """
        Run function, calculates the required edge data and stores it in the
        EdgeDataInterface instance.
        """
        edge_data = self.get_edge_data()

        self.edge_data_if.directed_edge_data = edge_data['directed_edge_data']
        self.edge_data_if.x_coordinates = edge_data['x_coordinates']
        self.edge_data_if.y_coordinates = edge_data['y_coordinates']
        self.edge_data_if.text_data = edge_data['text_data']

    def get_edge_data(self) -> dict:
        """
        Calculates the positions of the directed edges and the positions of
        the small markers used to create hover functionality for the edges,
        and the data required to make the hover text of the edges.
        :return dict: the data we need about the edges
        """
        directed_edge_data: list = []
        x_coordinates: list = []
        y_coordinates: list = []
        text_data: list = []

        for start, end in self.graph_edges:
            start_node_pos = self.positions[start]
            end_node_pos = self.positions[end]

            x_start = start_node_pos[0]
            x_end = end_node_pos[0]
            y_start = start_node_pos[1]
            y_end = end_node_pos[1]

            x_coordinates.append((x_start + x_end) / 2)
            y_coordinates.append((y_start + y_end) / 2)

            dx = x_end - x_start
            dy = y_end - y_start

            edge_data_dict = {
                'x_start': x_start + dx / 80,
                'y_start': y_start + dy / 80,
                'x_end': x_end - dx / 15,
                'y_end': y_end - dy / 15
            }

            directed_edge_data.append(edge_data_dict)

            start_name = self.rkm_station[float(start[0])]
            start_km = start[0]
            start_date = start[1]

            end_name = self.rkm_station[float(end[0])]
            end_km = end[0]
            end_date = end[1]

            text_data.append(
                (start_name, start_km, start_date, end_name, end_km, end_date)
            )

        edge_data = {
            'directed_edge_data': directed_edge_data,
            'x_coordinates': x_coordinates,
            'y_coordinates': y_coordinates,
            'text_data': text_data
        }

        return edge_data
