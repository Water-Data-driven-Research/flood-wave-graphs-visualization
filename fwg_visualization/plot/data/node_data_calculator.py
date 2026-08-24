from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.node_data_interface import (
    NodeDataInterface
)


class NodeDataCalculator:
    """
    Calculates the data required to make the node markers (node trace).
    """
    def __init__(self,
                 graph_data_if: GraphDataInterface,
                 rkm_station: dict,
                 vertex_data: dict,
                 level_group: dict):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        :param dict rkm_station: the dictionary that maps station positions on
               the river to their names
        :param dict vertex_data: data about the delta peaks, structure:
               {station1: {date1: {'value': value1, 'color': color1},
                           date2: {'value': value2, 'color': color2},
                           ...},
                station2: {date1: {'value': value1, 'color': color1},
                           date2: {'value': value2, 'color': color2},
                           ...},
                ...}
        :param dict level_group: the dictionary that maps station positions on
               the river to their level groups (values above which a water
               level is considered high)
        """
        self.graph_nodes = graph_data_if.graph_nodes
        self.positions = graph_data_if.positions
        self.rkm_station = rkm_station
        self.vertex_data = vertex_data
        self.level_group = level_group

        self.data_if = NodeDataInterface()

    def run(self):
        """
        Run function, calculates the required node data (the positions of the
        nodes and data required to make the hover text of the nodes) and
        stores it in the NodeDataInterface instance.
        """
        self.data_if.x_coordinates, self.data_if.y_coordinates = zip(*[
            (coord[0], coord[1]) for coord in self.positions.values()
        ])

        self.data_if.level_differences = []
        self.data_if.text_data = []

        for node in self.graph_nodes:
            node_date_str = node[1]
            station_name = self.rkm_station[float(node[0])]
            station_km = node[0]
            water_level = self.vertex_data[station_km][node_date_str]['value']
            station_level_group = self.level_group[node[0]]
            self.data_if.level_differences.append(water_level
                                                  - station_level_group)

            self.data_if.text_data.append(
                (node_date_str, station_name, station_km, water_level,
                 station_level_group)
            )
