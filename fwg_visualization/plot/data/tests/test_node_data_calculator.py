from datetime import datetime

import pytest

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)
from fwg_visualization.plot.data.node_data_calculator import (
    NodeDataCalculator
)


@pytest.fixture
def mock_nodes() -> list:
    """
    A list of potential nodes of a graph with which we can fill the mock graph
    data interface.
    :return list: the list of nodes
    """
    mock_nodes = []

    return mock_nodes


@pytest.fixture
def mock_edges() -> list:
    """
    A list of potential edges of a graph with which we can fill the mock graph
    data interface.
    :return list: the list of edges
    """
    mock_edges = []

    return mock_edges


@pytest.fixture
def mock_min_date() -> datetime:
    """
    A potential minimum node date of a graph with which we can fill the mock
    graph data interface.
    :return datetime: the minimum date
    """
    mock_min_date = datetime.min

    return mock_min_date


@pytest.fixture
def mock_stations() -> list:
    """
    A list of potential stations in a graph with which we can fill the mock
    graph data interface.
    :return list: the list of stations
    """
    mock_stations = []

    return mock_stations


@pytest.fixture
def mock_graph_data_if(mock_nodes: list,
                       mock_edges: list,
                       mock_min_date: datetime,
                       mock_stations: list) -> GraphDataInterface:
    """
    Creates a mock GraphDataInterface on which the NodeDataCalculator can be
    tested.
    :return GraphDataInterface: the mock GraphDataInterface to use for tests
    """
    mock_graph_data_if = GraphDataInterface()

    return mock_graph_data_if


@pytest.fixture
def mock_rkm_station() -> dict:
    """
    A potential mapping of station positions on the river to their names.
    :return dict: the potential mapping
    """
    mock_rkm_station = {}

    return mock_rkm_station


@pytest.fixture
def mock_level_group() -> dict:
    """
    A potential mapping of station positions on the river to their level
    groups (values above which a water level is considered high).
    :return dict: the potential mapping
    """
    mock_level_group = {}

    return mock_level_group


@pytest.fixture
def mock_node_data_if(mock_graph_data_if: GraphDataInterface,
                      mock_rkm_station: dict,
                      mock_level_group: dict) -> NodeDataInterface:
    """
    Extracts the necessary data from the mock GraphDataInterface with a
    NodeDataCalculator, then stores this data in a fixed NodeDataInterface,
    which we will use for testing
    :param GraphDataInterface mock_graph_data_if: the mock graph data interface
           which provides the data for testing
    :param dict mock_rkm_station: a potential mapping of station positions on
           the river to their names
    :param dict mock_level_group: a potential mapping of station positions on
           the river to their level groups (values above which a water level
           is considered high)
    :return NodeDataInterface: the fixed NodeDataInterface used for testing
    """
    mock_node_data_calc = NodeDataCalculator(graph_data_if=mock_graph_data_if,
                                             rkm_station=mock_rkm_station,
                                             level_group=mock_level_group)
    mock_node_data_calc.run()

    return mock_node_data_calc.node_data_if
