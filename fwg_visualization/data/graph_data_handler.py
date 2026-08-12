from datetime import datetime

import networkx as nx

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class GraphDataHandler:
    """
    This class preprocesses a flood wave graph or flood map for visualization.
    """
    def __init__(self, graph: nx.DiGraph):
        """
        Constructor.
        :param nx.DiGraph graph: the fwg or flood map to be preprocessed
        """
        self.graph_nodes = list(graph.nodes())
        self.graph_edges = list(graph.edges())

        self.graph_data_interface = GraphDataInterface()

    def run(self):
        """
        Run function, extracts the required data (min_date, stations) and
        stores it in the GraphDataInterface instance.
        """
        min_date = self.get_min_date()
        stations = self.get_stations()

        self.graph_data_interface.graph_nodes = self.graph_nodes
        self.graph_data_interface.graph_edges = self.graph_edges
        self.graph_data_interface.min_date = min_date
        self.graph_data_interface.stations = stations

    def get_min_date(self) -> datetime:
        """
        Finds the earliest date among the dates of the nodes of the flood wave
        graph or flood map.
        :return datetime: the earliest node date on the graph
        """
        min_date_temp = min(
            [node[1] for node in self.graph_nodes]
        )
        min_date = datetime.strptime(min_date_temp, '%Y-%m-%d')

        return min_date

    def get_stations(self) -> list:
        """
        Acquires and sorts a list of the stations in the flood wave graph or
        flood map.
        :return list: the list of the stations on the graph
        """
        stations = sorted(list(set(
            [float(node[0]) for node in self.graph_nodes]
        )))

        return stations
