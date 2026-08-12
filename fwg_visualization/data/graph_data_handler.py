from datetime import datetime, timedelta

import networkx as nx

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class GraphDataHandler:
    """
    This class preprocesses a flood wave graph or flood map for visualization.
    """
    def __init__(self,
                 graph: nx.DiGraph,
                 rkm_station: dict,
                 level_group: dict):
        """
        Constructor.
        :param nx.DiGraph graph: the fwg or flood map to be preprocessed
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        :param dict level_group: the dictionary that maps station positions on
               the river to their level groups (values above which a water
               level is considered high)
        """
        self.graph_nodes = list(graph.nodes())
        self.graph_edges = list(graph.edges())
        self.rkm_station = rkm_station
        self.level_group = level_group

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

        edge_data = self.create_edge_data()

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

    def create_edge_data(self) -> dict:
        """
        Creates the data required to make the arrows that are the edges of the
        directed graph, as well as data required to make very small markers
        (edge hover trace) to implement the hover functionality on edges.
        :return dict: contains the data, its keys are: 'directed_edge_data',
                'x_coords', 'y_coords' and 'text'
        """
        directed_edge_data = []
        x_coords = []
        y_coords = []
        text = []

        for start, end in self.graph_edges:
            x_start = self.pos[start][0]
            x_end = self.pos[end][0]
            y_start = self.pos[start][1]
            y_end = self.pos[end][1]

            x_coords.append((x_start + x_end) / 2)
            y_coords.append((y_start + y_end) / 2)

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

            text.append(
                (start_name, start_km, start_date, end_name, end_km, end_date)
            )

        edge_data = {
            'directed_edge_data': directed_edge_data,
            'x_coords': x_coords,
            'y_coords': y_coords,
            'text': text
        }

        return edge_data
