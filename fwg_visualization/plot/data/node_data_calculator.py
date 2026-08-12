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
        self.graph_nodes = graph_data_if.graph_nodes
        self.min_date = graph_data_if.min_date
        self.stations = graph_data_if.stations
        self.rkm_station = rkm_station
        self.level_group = level_group

        self.node_data_if = NodeDataInterface()

    def run(self):
        """
        Run function, calculates the required node data and instantiates a
        NodeDataInterface to store it.
        """
        node_data = self.get_node_data()

        self.node_data_if = NodeDataInterface(
            x_coordinates=node_data['x_coordinates'],
            y_coordinates=node_data['y_coordinates'],
            text_data=node_data['text_data']
        )

    def get_node_data(self):
        """
        Calculates the positions of the nodes and data required to make the
        hover text of the nodes.
        :return dict: the data we need about the nodes
        """
        station_to_idx = {
            station: i for i, station in enumerate(self.stations)
        }

        x_coordinates = []
        y_coordinates = []
        text_data = []

        for node in self.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coordinates.append((node_date - self.min_date).days)
            y_coordinates.append(station_to_idx[float(node[0])])

            node_date_str = node[1]
            station_name = self.rkm_station[float(node[0])]
            station_km = node[0]
            station_level_group = self.level_group[node[0]]

            text_data.append(
                (node_date_str, station_name, station_km, station_level_group)
            )

        node_data = {
            'x_coordinates': x_coordinates,
            'y_coordinates': y_coordinates,
            'text_data': text_data
        }

        return node_data
