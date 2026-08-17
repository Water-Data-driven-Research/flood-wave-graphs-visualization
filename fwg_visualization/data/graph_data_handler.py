from datetime import datetime

import networkx as nx

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class GraphDataHandler:
    """
    This class preprocesses a flood wave graph or flood map for visualization.
    """
    def __init__(self, graph: nx.DiGraph, manual_stations: list):
        """
        Constructor. If there are stations among the non-isolated graph nodes
        that are not given to the constructor as part of the manual_stations
        list, they will also appear on the y-axis.
        :param nx.DiGraph graph: the fwg or flood map to be preprocessed
        :param list manual_stations: the list of stations that should be
               displayed on the y-axis
        """
        self.graph_nodes = sorted(
            [node for node in set(graph.nodes()) - set(nx.isolates(graph))]
        )
        self.graph_edges = sorted(list(graph.edges()))
        self.manual_stations = manual_stations

        self.data_if = GraphDataInterface()

    def run(self):
        """
        Run function, extracts the required data (min_date, stations) and
        stores it in the GraphDataInterface instance.
        """
        min_date = self.get_min_date()
        stations = self.get_stations()
        positions = self.get_positions(min_date=min_date, stations=stations)

        self.data_if.graph_nodes = self.graph_nodes
        self.data_if.graph_edges = self.graph_edges
        self.data_if.min_date = min_date
        self.data_if.stations = stations
        self.data_if.positions = positions

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
        Acquires and sorts a list of the stations to be displayed, including
        both those in the flood wave graph or flood map, and those manually
        given.
        :return list: the list of the stations on the graph
        """
        stations = sorted(list(set(
            self.manual_stations
            + [float(node[0]) for node in self.graph_nodes]
        )))

        return stations

    def get_positions(self, min_date: datetime, stations: list) -> dict:
        """
        :param datetime min_date: the earlies date of the nodes of the plot
        :param list stations: the list of the stations on the graph
        Creates the positions dictionary, which maps the nodes to their
        eventual positions on the grid of the plot.
        """
        station_to_idx = {
            station: i for i, station in enumerate(stations)
        }

        positions: dict = {}

        for node in self.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coord = (node_date - min_date).days
            y_coord = station_to_idx[float(node[0])]

            positions[node] = (x_coord, y_coord)

        return positions
