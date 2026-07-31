from datetime import datetime

import networkx as nx
import pytest

from fwg_visualization.data.graph_data_handler import GraphDataHandler
from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


mock_graph = nx.DiGraph()

mock_graph.add_nodes_from(
    nodes_for_adding=[
        ('1.0', '2000-01-01'), ('1.0', '2000-01-06'),
        ('1.0', '2000-01-08'), ('2.0', '1999-12-31'),
        ('2.0', '2000-01-04'), ('3.0', '2000-01-03'),
        ('3.0', '1999-12-20'), ('5.0', '1999-12-24')
    ]
)

mock_graph.add_edges_from(
    ebunch_to_add=[
        (('2.0', '1999-12-31'), ('1.0', '2000-01-01'), {'slope': 1.0}),
        (('2.0', '2000-01-04'), ('1.0', '2000-01-06'), {'slope': 1.0}),
        (('3.0', '2000-01-03'), ('2.0', '2000-01-04'), {'slope': 1.0})
    ]
)

