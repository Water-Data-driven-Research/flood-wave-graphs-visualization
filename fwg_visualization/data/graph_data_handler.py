from datetime import datetime

import networkx as nx

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


class GraphDataHandler:
    """
    This class preprocesses a flood wave graph or flood map for visualization.
    """
    def __init__(self, data: dict):
        """
        Constructor.
        :param dict data: the data to be preprocessed (the fwg or flood map)
        """
        self.graph_nodes = data['graph'].nodes()
        self.data_interface = GraphDataInterface()
        self.extracted_data = dict()

        self.run()

    def run(self):
        """
        Run function, extracts the data and fills the self.extracted_data
        dictionary with it, then instantiates a GraphDataInterface.
        """
        self.extracted_data['min_date'] = self.get_min_date()
        self.extracted_data['stations'] = self.get_stations()
        self.extracted_data['pos'] = self.get_positions()

        self.data_interface = GraphDataInterface(data=self.extracted_data)

    def get_min_date(self) -> datetime:
        """
        Finds the earliest date among the dates of the nodes of the flood wave
        graph.
        :return datetime: the earliest date
        """
        min_date_temp = min(
            [node[1] for node in self.graph_nodes]
        )
        min_date = datetime.strptime(min_date_temp, '%Y-%m-%d')

        return min_date

    def get_stations(self) -> list:
        """
        Acquires and sorts a list of the stations in the flood wave graphs
        :return list: the
        """
        pass

    def get_positions(self) -> dict:
        """
        Creates a dictionary mapping the nodes to their eventual positions on
        the plot.
        :return dict: the dictionary of the nodes and their positions
        """
        pass
