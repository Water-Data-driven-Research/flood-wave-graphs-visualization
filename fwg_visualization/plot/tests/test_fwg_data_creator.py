from datetime import datetime

import pytest

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.fwg_data_creator import FWGDataCreator


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
def mock_vertex_data() -> dict:
    """
    Creates mock vertex data on which the codebase can be tested.
    :return dict: the mock vertex data on which we can run tests
    """
    mock_vertex_data = {
        '1.0': {'1998-06-24': {'value': 196, 'color': 'yellow'},
                '2000-01-01': {'value': 235, 'color': 'red'},
                '2000-01-14': {'value': 185, 'color': 'yellow'}},
        '2.0': {'1999-12-30': {'value': 188, 'color': 'red'},
                '2000-01-03': {'value': 178, 'color': 'red'},
                '2000-01-12': {'value': 151, 'color': 'yellow'}},
        '3.0': {'1999-12-24': {'value': 270, 'color': 'yellow'},
                '2000-01-02': {'value': 301, 'color': 'red'}},
        '5.0': {'1999-12-21': {'value': 75, 'color': 'yellow'}}
    }
    return mock_vertex_data


@pytest.fixture
def mock_level_groups() -> dict:
    """
    A potential mapping of station positions on the river to their level
    groups (values above which a water level is considered high).
    :return dict: the potential mapping
    """
    mock_level_groups = {
        '1.0': 200,
        '2.0': 178,
        '3.0': 295,
        '5.0': 79
    }

    return mock_level_groups


@pytest.fixture
def fwg_data_creator(mock_graph_data_if: GraphDataInterface,
                     mock_rkm_station: dict,
                     mock_vertex_data: dict,
                     mock_level_groups: dict) -> FWGDataCreator:
    """
    Creates the data necessary to plot the graph, which we will run tests on.
    :param GraphDataInterface mock_graph_data_if: the mock graph data interface
           which provides the data for testing
    :param dict mock_rkm_station: a potential mapping of station positions on
           the river to their names
    :param dict mock_vertex_data: potential data about the delta peaks,
           structure: {station1: {date1: {'value': value1, 'color': color1},
                                  date2: {'value': value2, 'color': color2},
                                  ...},
                       station2: {date1: {'value': value1, 'color': color1},
                                  date2: {'value': value2, 'color': color2},
                                  ...},
                       ...}
    :param dict mock_level_groups: a potential mapping of station positions on
           the river to their level groups (values above which a water level
           is considered high)
    :return FWGDataCreator: the fixed FWGDataCreator used for testing
    """
    fwg_data_creator = FWGDataCreator(graph_data_if=mock_graph_data_if,
                                      rkm_station=mock_rkm_station,
                                      vertex_data=mock_vertex_data,
                                      level_groups=mock_level_groups)
    fwg_data_creator.run()

    return fwg_data_creator


@pytest.mark.parametrize('expected_x_coordinates,'
                         'expected_y_coordinates,'
                         'expected_level_differences,'
                         'expected_text_data', [
                             ((11, 24, 9, 13, 22, 3, 12, 0),
                              (0, 0, 1, 1, 1, 2, 2, 3),
                              [35, -15, 10, 0, -27, -25, 6, -4],
                              [('2000-01-01', 'Station One', '1.0', 235, 200),
                               ('2000-01-14', 'Station One', '1.0', 185, 200),
                               ('1999-12-30', 'Station Two', '2.0', 188, 178),
                               ('2000-01-03', 'Station Two', '2.0', 178, 178),
                               ('2000-01-12', 'Station Two', '2.0', 151, 178),
                               ('1999-12-24', 'Station Three', '3.0', 270,
                                295),
                               ('2000-01-02', 'Station Three', '3.0', 301,
                                295),
                               ('1999-12-21', 'Station Four', '5.0', 75, 79)])
                         ])
def test_node_data(fwg_data_creator: FWGDataCreator,
                   expected_x_coordinates: tuple,
                   expected_y_coordinates: tuple,
                   expected_level_differences: list,
                   expected_text_data: list):
    """
    Tests whether the positions of the graph nodes and the text data were
    calculated correctly or not.
    :param FWGDataCreator fwg_data_creator: contains the calculated positions
           of graph nodes and text data
    :param tuple expected_x_coordinates: the expected correct tuple of x-
           coordinates
    :param tuple expected_y_coordinates: the expected correct tuple of y-
           coordinates
    :param list expected_level_differences: the expect correct list of water
           level differences from the level group
    :param list expected_text_data: the expected correct text data
    """
    node_data_if = fwg_data_creator.node_data_if

    assert node_data_if.x_coordinates == expected_x_coordinates
    assert node_data_if.y_coordinates == expected_y_coordinates
    assert node_data_if.level_differences == expected_level_differences
    assert node_data_if.text_data == expected_text_data


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
def test_axis_data(fwg_data_creator: FWGDataCreator,
                   expected_x_ticks: list,
                   expected_x_tick_labels: list,
                   expected_y_ticks: list,
                   expected_y_tick_labels: list):
    """
    Tests whether the axis data was calculated correctly or not.
    :param FWGDataCreator fwg_data_creator: contains the calculated axis data
    :param list expected_x_ticks: the expected correct list of x-axis ticks
    :param list expected_x_tick_labels: the expected correct list of x-tick
           labels
    :param list expected_y_ticks: the expected correct list of y-axis ticks
    :param list expected_y_tick_labels: the expected correct list of y-tick
           labels
    """
    axis_data_if = fwg_data_creator.axis_data_if

    assert axis_data_if.x_ticks == expected_x_ticks
    assert axis_data_if.x_tick_labels == expected_x_tick_labels
    assert axis_data_if.y_ticks == expected_y_ticks
    assert axis_data_if.y_tick_labels == expected_y_tick_labels


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
def test_edge_data(fwg_data_creator: FWGDataCreator,
                   expected_edge_data: list):
    """
    Tests whether the positions of the graph edges were calculated correctly or
    not.
    :param FWGDataCreator fwg_data_creator: contains the calculated positions
           of graph directed edges
    :param list expected_edge_data: the expected correct list of directed edge
           positions
    """
    edge_data_if = fwg_data_creator.edge_data_if

    assert edge_data_if.directed_edge_data == expected_edge_data
