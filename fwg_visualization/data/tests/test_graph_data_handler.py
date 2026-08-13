from datetime import datetime

import networkx as nx
import pytest

from fwg_visualization.data.graph_data_handler import GraphDataHandler
from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)


@pytest.fixture
def mock_graph() -> nx.DiGraph:
    """
    Creates a mock graph on which the codebase can be tested.
    :return nx.DiGraph: the mock graph on which we can run tests
    """
    mock_graph = nx.DiGraph()
    mock_graph.add_nodes_from(
        nodes_for_adding=[
            ('1.0', '2000-01-01'), ('1.0', '2000-01-06'),
            ('3.0', '2000-01-03'), ('1.0', '2000-01-08'),
            ('2.0', '1999-12-31'), ('3.0', '1999-12-20'),
            ('2.0', '2000-01-04'), ('5.0', '1999-12-24')
        ]
    )
    mock_graph.add_edges_from(
        ebunch_to_add=[
            (('2.0', '1999-12-31'), ('1.0', '2000-01-01'), {'slope': 1.0}),
            (('3.0', '2000-01-03'), ('2.0', '2000-01-04'), {'slope': 1.0}),
            (('2.0', '2000-01-04'), ('1.0', '2000-01-06'), {'slope': 1.0})
        ]
    )
    return mock_graph


@pytest.fixture
def graph_data_interface(mock_graph: nx.DiGraph) -> GraphDataInterface:
    """
    Extracts the necessary data from the mock graph with a GraphDataHandler,
    which stores this data in a fixed GraphDataInterface, which we will use
    for testing.
    :param nx.DiGraph mock_graph: the mock graph on which we run the tests
    :return GraphDataInterface: the fixed data interface used for testing
    """
    graph_data_handler = GraphDataHandler(
        graph=mock_graph
    )
    graph_data_handler.run()

    return graph_data_handler.graph_data_interface


@pytest.mark.parametrize('expected_graph_nodes', [
    [('1.0', '2000-01-01'), ('1.0', '2000-01-06'), ('1.0', '2000-01-08'),
     ('2.0', '1999-12-31'), ('2.0', '2000-01-04'), ('3.0', '1999-12-20'),
     ('3.0', '2000-01-03'), ('5.0', '1999-12-24')]
])
def test_nodes(graph_data_interface: GraphDataInterface,
               expected_graph_nodes: list):
    """
    Tests whether the nodes of the graph are acquired as intended.
    :param GraphDataInterface graph_data_interface: contains the calculated
           list of graph nodes
    :param list expected_graph_nodes: the expected correct list of graph nodes
    """
    assert graph_data_interface.graph_nodes == expected_graph_nodes


@pytest.mark.parametrize('expected_graph_edges', [
    [(('2.0', '1999-12-31'), ('1.0', '2000-01-01')),
     (('2.0', '2000-01-04'), ('1.0', '2000-01-06')),
     (('3.0', '2000-01-03'), ('2.0', '2000-01-04'))]
])
def test_edges(graph_data_interface: GraphDataInterface,
               expected_graph_edges: list):
    """
    Tests whether the nodes of the graph are acquired as intended.
    :param GraphDataInterface graph_data_interface: contains the calculated
           list of graph edges
    :param list expected_graph_edges: the expected correct list of graph edges
    """
    assert graph_data_interface.graph_edges == expected_graph_edges


@pytest.mark.parametrize('expected_min_date', [
    datetime(year=1999, month=12, day=20)
])
def test_min_date(graph_data_interface: GraphDataInterface,
                  expected_min_date: datetime):
    """
    Tests whether the minimum date is correctly calculated or not.
    :param GraphDataInterface graph_data_interface: contains the results of
           the minimum date calculation
    :param datetime expected_min_date: the expected correct result for the
           minimum date calculation
    """
    assert graph_data_interface.min_date == expected_min_date


@pytest.mark.parametrize('expected_stations', [
    [1.0, 2.0, 3.0, 5.0]
])
def test_stations(graph_data_interface: GraphDataInterface,
                  expected_stations: list):
    """
    Tests whether the list of stations is correctly acquired or not.
    :param GraphDataInterface graph_data_interface: contains the acquired list
           of stations
    :param list expected_stations: the expected correct list of stations
    """
    assert graph_data_interface.stations == expected_stations


@pytest.mark.parametrize('expected_positions', [
    {
        ('1.0', '2000-01-01'): (12, 0),
        ('1.0', '2000-01-06'): (17, 0),
        ('3.0', '2000-01-03'): (14, 2),
        ('1.0', '2000-01-08'): (19, 0),
        ('2.0', '1999-12-31'): (11, 1),
        ('3.0', '1999-12-20'): (0, 2),
        ('2.0', '2000-01-04'): (15, 1),
        ('5.0', '1999-12-24'): (4, 3)
    }
])
def test_positions(graph_data_interface: GraphDataInterface,
                   expected_positions: dict):
    """
    Tests whether the future positions on the grid are correctly calculated or
    not.
    :param GraphDataInterface graph_data_interface: contains the calculated
           mapping of nodes to their eventual positions on the grid
    :param dict expected_positions: the expected correct mapping of nodes to
           their eventual positions on the grid
    """
    assert graph_data_interface.positions == expected_positions
