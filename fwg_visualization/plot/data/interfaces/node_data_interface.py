from dataclasses import dataclass


@dataclass
class NodeDataInterface:
    """
    Class for storing data calculated in a NodeDataCalculator class.
    :param dict positions: the dictionary mapping the nodes to their positions
    :param list text_data: data required to make the hover texts of the nodes
    """
    positions: dict = None
    text_data: list = None
