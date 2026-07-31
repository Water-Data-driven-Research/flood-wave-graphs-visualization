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


@pytest.fixture
def graph_data_interface() -> GraphDataInterface:
    """
    Extracts the necessary data from the mock graph with a GraphDataHandler,
    which stores this data in a fixed GraphDataInterface, which we will use
    for testing.
    :return GraphDataInterface: the fixed data interface used for testing
    """
    graph_data_handler = GraphDataHandler(
        graph=mock_graph
    )

    return graph_data_handler.graph_data_interface


@pytest.mark.parametrize('expected_min_date', [
    datetime(year=1999, month=12, day=20)
])
def test_min_date(graph_data_interface: GraphDataInterface,
                  expected_min_date: datetime
                  ):
    assert graph_data_interface.min_date == expected_min_date


@pytest.mark.parametrize('expected_stations', [
    [1.0, 2.0, 3.0, 5.0]
])
def test_stations(graph_data_interface: GraphDataInterface,
                  expected_stations: list
                  ):
    assert graph_data_interface.stations == expected_stations


@pytest.mark.parametrize('expected_pos', [
    {
        ('1.0', '2000-01-01'): (12, 0),
        ('1.0', '2000-01-06'): (17, 0),
        ('1.0', '2000-01-08'): (19, 0),
        ('2.0', '1999-12-31'): (11, 1),
        ('2.0', '2000-01-04'): (15, 1),
        ('3.0', '2000-01-03'): (14, 2),
        ('3.0', '1999-12-20'): (0, 2),
        ('5.0', '1999-12-24'): (4, 3)
    }
])
def test_pos(graph_data_interface: GraphDataInterface,
             expected_pos: dict
             ):
    assert graph_data_interface.pos == expected_pos
