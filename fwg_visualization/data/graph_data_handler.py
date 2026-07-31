from datetime import datetime

import networkx as nx
import pandas as pd
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
        pass
