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
               the river to their level groups (value above which a water
               level is considered high)
        """
        self.graph_nodes = graph.nodes()
        self.rkm_station = rkm_station
        self.level_group = level_group

        self.graph_data_interface = GraphDataInterface()
        self.min_date: datetime = datetime.min
        self.stations: list = []
        self.pos: dict = {}

    def run(self):
        """
        Run function, extracts the required data (min_date, stations, pos),
        then instantiates a GraphDataInterface to store this data.
        """
        self.get_min_date()
        self.get_stations()
        self.get_positions()

        axis_data = self.create_axis_data()

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

    def get_positions(self):
        """
        Fills the self.pos dictionary, which maps the nodes to their eventual
        positions on the grid of the plot.
        """
        station_to_idx = {
            station: i for i, station in enumerate(self.stations)
        }

        for node in self.graph_nodes:
            node_date = datetime.strptime(node[1], '%Y-%m-%d')

            x_coord = (node_date - self.min_date).days
            y_coord = station_to_idx[float(node[0])]

            self.pos[node] = (x_coord, y_coord)

    def create_axis_data(self) -> dict:
        """
        Creates the data to be put on the axes that will be displayed on the
        figure (x-axis and y-axis ticks and their labels).
        :return dict: the data, its keys are: 'x_ticks', 'x_tick_labels',
                'y_ticks', 'y_tick_labels'
        """
        min_x = min([n[0] for n in self.pos.values()])
        max_x = max([n[0] for n in self.pos.values()])

        no_of_ticks = min(max_x - min_x, 20)
        x_ticks = list(range(
            int(min_x),
            int(max_x) + 1,
            int(max_x / no_of_ticks)
        ))
        x_tick_labels = [
            (self.min_date + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in x_ticks
        ]

        y_ticks = list(range(len(self.stations)))

        axis_data = {
            'x_ticks': x_ticks,
            'x_tick_labels': x_tick_labels,
            'y_ticks': y_ticks,
            'y_tick_labels': y_ticks
        }

        return axis_data

    def create_node_data(self) -> dict:
        """
        Creates the data required to make the node markers (node trace).
        :return dict: the data, its keys are: 'x_coords', 'y_coords', 'text'
        """
        x_coords, y_coords = zip(*[
            (coord[0], coord[1]) for coord in self.pos.values()
        ])

        text = [(node[1], self.rkm_station[float(node[0])],
                 node[0], self.level_group[node[0]])
                for node in self.graph_nodes]

        node_data = {
            'x_coords': x_coords,
            'y_coords': y_coords,
            'text': text
        }

        return node_data

    def create_edge_data(self) -> dict:
        """
        Creates the arrows that are the edges of the directed graph, as well
        as markers to create the hover function.
        :return dict: contains the data, its keys are: 'arrows' (the value is
                the list containing every directed edge, each stored as a
                dictionary), and 'markers' (the value is another dictionary,
                whose keys are 'x_coords', 'y_coords' and 'text')
        """
        pass
