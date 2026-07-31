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
        self.min_date = None
        self.stations = []
        self.pos = dict()

        self.run()

    def run(self):
        """
        Run function, extracts the data and fills the self.extracted_data
        dictionary with it, then instantiates a GraphDataInterface.
        """
        self.min_date = self.get_min_date()
        self.stations = self.get_stations()
        self.pos = self.get_positions()

        self.graph_data_interface = GraphDataInterface(
            min_date=self.min_date,
            stations=self.stations,
            pos=self.pos
        )

    def get_min_date(self) -> datetime:
        """
        Finds the earliest date among the dates of the nodes of the flood wave
        graph or flood map.
        :return datetime: the earliest date
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
        :return list: the list of the stations in the graph
        """
        stations = sorted(
            [float(node[0]) for node in self.graph_nodes]
        )

        return stations

    def get_positions(self) -> dict:
        """
        Creates a dictionary mapping the nodes to their eventual positions on
        the grid of the plot.
        :return dict: the dictionary of the nodes and their positions
        """
        station_to_idx = {
            station: i for i, station in enumerate(
                self.stations
            )
        }

        positions = dict()

        for node in self.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coord = (node_date - self.min_date).days
            y_coord = station_to_idx[float(node[0])]

            positions[node] = (x_coord, y_coord)

        return positions
