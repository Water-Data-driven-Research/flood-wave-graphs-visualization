from dataclasses import dataclass


@dataclass
class NodeDataInterface:
    """
    Class for storing data calculated in a NodeDataCalculator class.
    :param list x_coordinates: the x-coordinates of the nodes
    :param list y_coordinates: the y-coordinates of the nodes
    :param list text_data: data required to make the hover texts of the nodes
    """
    x_coordinates: list = None
    y_coordinates: list = None
    text_data: list = None
