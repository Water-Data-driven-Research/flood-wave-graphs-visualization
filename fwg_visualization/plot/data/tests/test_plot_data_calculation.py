from datetime import datetime

import pytest

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.axis_data_calculator import AxisDataCalculator
from fwg_visualization.plot.data.edge_data_calculator import EdgeDataCalculator
from fwg_visualization.plot.data.interfaces.axis_data_interface import (
    AxisDataInterface
)
from fwg_visualization.plot.data.interfaces.edge_data_interface import (
    EdgeDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)
from fwg_visualization.plot.data.node_data_calculator import NodeDataCalculator


@pytest.fixture
def mock_nodes() -> list:
    """
    A list of potential nodes of a graph with which we can fill the mock graph
    data interface.
    :return list: the list of nodes
    """
    mock_nodes = [('1.0', '2000-01-01'), ('1.0', '2000-01-14'),
                  ('3.0', '2000-01-02'), ('2.0', '1999-12-30'),
                  ('2.0', '2000-01-03'), ('3.0', '1999-12-24'),
                  ('2.0', '2000-01-12'), ('5.0', '1999-12-21')]

    return mock_nodes


@pytest.fixture
def mock_edges() -> list:
    """
    A list of potential edges of a graph with which we can fill the mock graph
    data interface.
    :return list: the list of edges
    """
    mock_edges = [(('2.0', '1999-12-30'), ('1.0', '2000-01-01')),
                  (('3.0', '2000-01-02'), ('2.0', '2000-01-03')),
                  (('2.0', '2000-01-12'), ('1.0', '2000-01-14')),
                  (('5.0', '1999-12-21'), ('3.0', '1999-12-24'))]

    return mock_edges


@pytest.fixture
def mock_min_date() -> datetime:
    """
    A potential minimum node date of a graph with which we can fill the mock
    graph data interface.
    :return datetime: the minimum date
    """
    mock_min_date = datetime.strptime('1999-12-21', '%Y-%m-%d')

    return mock_min_date


@pytest.fixture
def mock_stations() -> list:
    """
    A list of potential stations in a graph with which we can fill the mock
    graph data interface.
    :return list: the list of stations
    """
    mock_stations = [1.0, 2.0, 3.0, 5.0]

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
    mock_graph_data_if = GraphDataInterface(graph_nodes=mock_nodes,
                                            graph_edges=mock_edges,
                                            min_date=mock_min_date,
                                            stations=mock_stations)

    return mock_graph_data_if


@pytest.fixture
def mock_rkm_station() -> dict:
    """
    A potential mapping of station positions on the river to their names.
    :return dict: the potential mapping
    """
    mock_rkm_station = {
        1.0: 'Station One',
        2.0: 'Station Two',
        3.0: 'Station Three',
        5.0: 'Station Four'
    }

    return mock_rkm_station


@pytest.fixture
def mock_level_group() -> dict:
    """
    A potential mapping of station positions on the river to their level
    groups (values above which a water level is considered high).
    :return dict: the potential mapping
    """
    mock_level_group = {
        '1.0': 200,
        '2.0': 178,
        '3.0': 295,
        '5.0': 79
    }

    return mock_level_group


@pytest.fixture
def node_data_interface(mock_graph_data_if: GraphDataInterface,
                        mock_rkm_station: dict,
                        mock_level_group: dict) -> NodeDataInterface:
    """
    Extracts the necessary data from the mock GraphDataInterface with a
    NodeDataCalculator, then stores this data in a fixed NodeDataInterface,
    which we will use for testing.
    :param GraphDataInterface mock_graph_data_if: the mock graph data interface
           which provides the data for testing
    :param dict mock_rkm_station: a potential mapping of station positions on
           the river to their names
    :param dict mock_level_group: a potential mapping of station positions on
           the river to their level groups (values above which a water level
           is considered high)
    :return NodeDataInterface: the fixed NodeDataInterface used for testing
    """
    node_data_calculator = NodeDataCalculator(graph_data_if=mock_graph_data_if,
                                              rkm_station=mock_rkm_station,
                                              level_group=mock_level_group)
    node_data_calculator.run()

    return node_data_calculator.node_data_if


@pytest.fixture
def axis_data_interface(
        mock_graph_data_if: GraphDataInterface) -> AxisDataInterface:
    """
    Extracts the necessary data from the mock GraphDataInterface and the
    NodeDataInterface with an AxisDataCalculator, then stores this data in a
    fixed AxisDataInterface, which we will use for testing.
    :param GraphDataInterface mock_graph_data_if: the mock graph data interface
           which provides the data for testing
    :return AxisDataInterface: the fixed AxisDataInterface used for testing
    """
    axis_data_calculator = AxisDataCalculator(graph_data_if=mock_graph_data_if)
    axis_data_calculator.run()

    return axis_data_calculator.axis_data_if


@pytest.fixture
def edge_data_interface(mock_graph_data_if: GraphDataInterface,
                        mock_rkm_station: dict) -> EdgeDataInterface:
    """
    Extracts the necessary data from the mock GraphDataInterface and the
    NodeDataInterface with an EdgeDataCalculator, then stores this data in a
    fixed EdgeDataInterface, which we will use for testing.
    :param GraphDataInterface mock_graph_data_if: the mock graph data interface
           which provides the data for testing
    :param dict mock_rkm_station: a potential mapping of station positions on
           the river to their names
    :return EdgeDataInterface: the fixed EdgeDataInterface used for testing
    """
    edge_data_calculator = EdgeDataCalculator(graph_data_if=mock_graph_data_if,
                                              rkm_station=mock_rkm_station)
    edge_data_calculator.run()

    return edge_data_calculator.edge_data_if


@pytest.mark.parametrize('expected_x_coordinates,'
                         'expected_y_coordinates,'
                         'expected_text_data', [
                             ([11, 24, 12, 9, 13, 3, 22, 0],
                              [0, 0, 2, 1, 1, 2, 1, 1, 3],
                              [
                                  ('2000-01-01', 'Station One', '1.0', 200),
                                  ('2000-01-14', 'Station One', '1.0', 200),
                                  ('2000-01-02', 'Station Three', '3.0', 295),
                                  ('1999-12-30', 'Station Two', '2.0', 178),
                                  ('2000-01-03', 'Station Two', '2.0', 178),
                                  ('1999-12-24', 'Station Three', '3.0', 295),
                                  ('2000-01-12', 'Station Two', '2.0', 178),
                                  ('1999-12-21', 'Station Four', '5.0', 79)
                              ])
                         ])
def test_node_data(node_data_interface: NodeDataInterface,
                   expected_x_coordinates: list,
                   expected_y_coordinates: list,
                   expected_text_data: list):
    """
    Tests whether the positions of the graph nodes and the text data were
    calculated correctly or not.
    :param NodeDataInterface node_data_interface: contains the calculated
           positions of graph nodes
    :param list expected_x_coordinates: the expected correct list of x-
           coordinates
    :param list expected_y_coordinates: the expected correct list of y-
           coordinates
    :param list expected_text_data: the expected correct text data
    """
    assert node_data_interface.x_coordinates == expected_x_coordinates
    assert node_data_interface.y_coordinates == expected_y_coordinates
    assert node_data_interface.text_data == expected_text_data
