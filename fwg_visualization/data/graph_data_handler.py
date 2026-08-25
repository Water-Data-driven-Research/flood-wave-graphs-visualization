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
        graph_nodes = sorted(
            [node for node in set(graph.nodes()) - set(nx.isolates(graph))]
        )
        graph_edges = sorted(list(graph.edges()))
        self.manual_stations = manual_stations

        self.data_if = GraphDataInterface(graph_nodes=graph_nodes,
                                          graph_edges=graph_edges)

    def run(self):
        """
        Run function, extracts the required data (min_date, stations,
        positions) and stores it in the GraphDataInterface instance.
        """
        self.get_min_date()
        self.get_stations()
        self.get_positions()

    def get_min_date(self):
        """
        Finds the earliest date among the dates of the nodes of the flood wave
        graph or flood map, and stores it in the GraphDataInterface instance.
        """
        min_date_temp = min([node[1] for node in self.data_if.graph_nodes])
        self.data_if.min_date = datetime.strptime(min_date_temp,
                                                  '%Y-%m-%d')

    def get_stations(self):
        """
        Acquires and sorts a list of the stations to be displayed, including
        both those in the flood wave graph or flood map, and those manually
        given, and stores this list in the GraphDataInterface instance.
        """
        self.data_if.stations = sorted(list(set(
            self.manual_stations
            + [float(node[0]) for node in self.data_if.graph_nodes]
        )))

    def get_positions(self):
        """
        Creates a dictionary mapping the nodes of the graph to their eventual
        positions on the grid, and stores it in the GraphDataInterface
        instance.
        """
        station_to_idx = {
            station: i for i, station in enumerate(self.data_if.stations)
        }

        self.data_if.positions = {}

        for node in self.data_if.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coord = (node_date - self.data_if.min_date).days
            y_coord = station_to_idx[float(node[0])]

            self.data_if.positions[node] = (x_coord, y_coord)
