from datetime import datetime, timedelta

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
        self.min_date: datetime = datetime.min
        self.stations: list = []

    def run(self):
        """
        Run function, extracts the required data (min_date, stations, pos),
        uses that data to prepare precise data for graph creation,
        then instantiates a GraphDataInterface to store this precise data.
        """
        self.get_min_date()
        self.get_stations()

        self.graph_data_interface = GraphDataInterface(
            graph_nodes=self.graph_nodes,
            graph_edges=self.graph_edges,
            min_date=self.min_date,
            stations=self.stations
        )

    def get_min_date(self):
        """
        Fills the self.min_date datetime by finding the earliest date among
        the dates of the nodes of the flood wave graph or flood map.
        """
        min_date_temp = min(
            [node[1] for node in self.graph_nodes]
        )
        self.min_date = datetime.strptime(min_date_temp, '%Y-%m-%d')

    def get_stations(self):
        """
        Fills the self.stations list by acquiring and sorting a list of the
        stations in the flood wave graph or flood map.
        """
        self.stations = sorted(list(set(
            [float(node[0]) for node in self.graph_nodes]
        )))
