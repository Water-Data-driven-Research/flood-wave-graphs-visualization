from dataclasses import dataclass


@dataclass
class EdgeDataInterface:
    """
    Class for storing data calculated in a GraphDataCalculator class.
    :param list directed_edge_data: the positions of the directed edges
    """
    directed_edge_data: list = None
