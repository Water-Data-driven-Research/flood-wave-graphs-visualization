from dataclasses import dataclass


@dataclass
class GraphDataInterface:
    """
    Class for storing data preprocessed in a GraphDataHandler class.
    :param dict axis_data: data to create the axes of the plot
    :param dict node_data: data to create the nodes of the graph
    :param dict edge_data: data to create the edges of the graph
    """
    axis_data: dict = None
    node_data: dict = None
    edge_data: dict = None
