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
        self.graph_nodes = graph.nodes()

        self.graph_data_interface = GraphDataInterface()
        self.min_date: datetime = datetime.min
        self.stations: list = []
        self.pos: dict = {}

    def run(self):
        """
        Run function, extracts the required data (min_date, stations, pos) and
        fills the member variables with it, then instantiates a
        GraphDataInterface to store this data.
        """
        self.stations = self.get_stations()
        self.pos = self.get_positions()
        self.get_min_date()
        self.get_stations()

        self.graph_data_interface = GraphDataInterface(
            min_date=self.min_date,
            stations=self.stations,
            pos=self.pos
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

        return stations

    def get_positions(self) -> dict:
        """
        Creates a dictionary mapping the nodes to their eventual positions on
        the grid of the plot.
        :return dict: the dictionary of the nodes and their positions
        """
        station_to_idx = {
            station: i for i, station in enumerate(self.stations)
        }

        positions = dict()

        for node in self.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coord = (node_date - self.min_date).days
            y_coord = station_to_idx[float(node[0])]

            positions[node] = (x_coord, y_coord)

        return positions
