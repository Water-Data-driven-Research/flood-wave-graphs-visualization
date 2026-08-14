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
    A potential list of nodes of a graph.
    :return list: the list of nodes
    """
    mock_nodes = [('1.0', '2000-01-01'), ('1.0', '2000-01-14'),
                  ('2.0', '1999-12-30'), ('2.0', '2000-01-03'),
                  ('2.0', '2000-01-12'), ('3.0', '1999-12-24'),
                  ('3.0', '2000-01-02'), ('5.0', '1999-12-21')]

    return mock_nodes


@pytest.fixture
def mock_edges() -> list:
    """
    A potential list of edges of a graph.
    :return list: the list of edges
    """
    mock_edges = [(('2.0', '1999-12-30'), ('1.0', '2000-01-01')),
                  (('2.0', '2000-01-12'), ('1.0', '2000-01-14')),
                  (('3.0', '2000-01-02'), ('2.0', '2000-01-03')),
                  (('5.0', '1999-12-21'), ('3.0', '1999-12-24'))]

    return mock_edges


@pytest.fixture
def mock_min_date() -> datetime:
    """
    A potential minimum node date of a graph.
    :return datetime: the minimum date
    """
    mock_min_date = datetime.strptime('1999-12-21', '%Y-%m-%d')

    return mock_min_date


@pytest.fixture
def mock_stations() -> list:
    """
    A potential list of stations in a graph.
    :return list: the list of stations
    """
    mock_stations = [1.0, 2.0, 3.0, 5.0]

    return mock_stations


@pytest.fixture
def mock_positions() -> dict:
    """
    A potential mapping of nodes to their eventual positions on the grid.
    :return datetime: the minimum date
    """
    mock_positions = {
        ('1.0', '2000-01-01'): (11, 0),
        ('1.0', '2000-01-14'): (24, 0),
        ('2.0', '1999-12-30'): (9, 1),
        ('2.0', '2000-01-03'): (13, 1),
        ('2.0', '2000-01-12'): (22, 1),
        ('3.0', '1999-12-24'): (3, 2),
        ('3.0', '2000-01-02'): (12, 2),
        ('5.0', '1999-12-21'): (0, 3)
    }

    return mock_positions


@pytest.fixture
def mock_graph_data_if(mock_nodes: list,
                       mock_edges: list,
                       mock_min_date: datetime,
                       mock_stations: list,
                       mock_positions: dict) -> GraphDataInterface:
    """
    Creates a mock GraphDataInterface on which the NodeDataCalculator can be
    tested.
    :param list mock_nodes: a potential list of nodes of a graph
    :param list mock_edges: a potential list of edges of a graph
    :param list mock_min_date: a potential minimum node date of a graph.
    :param list mock_stations: a potential list of stations in a graph.
    :param list mock_positions: a potential mapping of nodes to their eventual
            positions on the  grid
    :return GraphDataInterface: the mock GraphDataInterface to use for tests
    """
    mock_graph_data_if = GraphDataInterface(graph_nodes=mock_nodes,
                                            graph_edges=mock_edges,
                                            min_date=mock_min_date,
                                            stations=mock_stations,
                                            positions=mock_positions)

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
                             ((11, 24, 9, 13, 22, 3, 12, 0),
                              (0, 0, 1, 1, 1, 2, 2, 3),
                              [
                                  ('2000-01-01', 'Station One', '1.0', 200),
                                  ('2000-01-14', 'Station One', '1.0', 200),
                                  ('1999-12-30', 'Station Two', '2.0', 178),
                                  ('2000-01-03', 'Station Two', '2.0', 178),
                                  ('2000-01-12', 'Station Two', '2.0', 178),
                                  ('1999-12-24', 'Station Three', '3.0', 295),
                                  ('2000-01-02', 'Station Three', '3.0', 295),
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


@pytest.mark.parametrize('expected_x_ticks,'
                         'expected_x_tick_labels,'
                         'expected_y_ticks,'
                         'expected_y_tick_labels',
                         [
                             ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                               14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                              ['1999-12-21', '1999-12-22', '1999-12-23',
                               '1999-12-24', '1999-12-25', '1999-12-26',
                               '1999-12-27', '1999-12-28', '1999-12-29',
                               '1999-12-30', '1999-12-31', '2000-01-01',
                               '2000-01-02', '2000-01-03', '2000-01-04',
                               '2000-01-05', '2000-01-06', '2000-01-07',
                               '2000-01-08', '2000-01-09', '2000-01-10',
                               '2000-01-11', '2000-01-12', '2000-01-13',
                               '2000-01-14'],
                              [0, 1, 2, 3],
                              [1.0, 2.0, 3.0, 5.0])
                         ])
def test_axis_data(axis_data_interface: AxisDataInterface,
                   expected_x_ticks: list,
                   expected_x_tick_labels: list,
                   expected_y_ticks: list,
                   expected_y_tick_labels: list):
    """
    Tests whether the axis data was calculated correctly or not.
    :param AxisDataInterface axis_data_interface: contains the calculated
           axis data
    :param list expected_x_ticks: the expected correct list of x-axis ticks
    :param list expected_x_tick_labels: the expected correct list of x-tick
           labels
    :param list expected_y_ticks: the expected correct list of y-axis ticks
    :param list expected_y_tick_labels: the expected correct list of y-tick
           labels
    """
    assert axis_data_interface.x_ticks == expected_x_ticks
    assert axis_data_interface.x_tick_labels == expected_x_tick_labels
    assert axis_data_interface.y_ticks == expected_y_ticks
    assert axis_data_interface.y_tick_labels == expected_y_tick_labels


@pytest.mark.parametrize('expected_edge_data,', [
    [
        {
            'x_start': 9.025,
            'y_start': 0.9875,
            'x_end': 10.866667,
            'y_end': 0.066667
        },
        {
            'x_start': 22.025,
            'y_start': 0.9875,
            'x_end': 23.866667,
            'y_end': 0.066667
        },
        {
            'x_start': 12.0125,
            'y_start': 1.9875,
            'x_end': 12.933333,
            'y_end': 1.066667
        },
        {
            'x_start': 0.0375,
            'y_start': 2.9875,
            'x_end': 2.8,
            'y_end': 2.066667
        }
    ]
])
def test_edge_data(edge_data_interface: EdgeDataInterface,
                   expected_edge_data: list):
    """
    Tests whether the positions of the graph nodes and the text data were
    calculated correctly or not.
    :param EdgeDataInterface edge_data_interface: contains the calculated
           positions of graph directed edges
    :param list expected_edge_data: the expected correct list of directed edge
           positions
    """
    assert edge_data_interface.directed_edge_data == expected_edge_data
