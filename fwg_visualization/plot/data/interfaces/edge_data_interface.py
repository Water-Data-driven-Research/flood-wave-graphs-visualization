from dataclasses import dataclass


@dataclass
class EdgeDataInterface:
    """
    Class for storing data calculated in a GraphDataCalculator class.
    :param list directed_edge_data: the positions of the directed edges
    :param list x_coordinates: the x-coordinates of the small edge markers
    :param list y_coordinates: the y-coordinates of the small edge markers
    :param list text_data: data required to make the hover texts of the edges
    """
    directed_edge_data: list = None
    x_coordinates: list = None
    y_coordinates: list = None
    text_data: list = None

