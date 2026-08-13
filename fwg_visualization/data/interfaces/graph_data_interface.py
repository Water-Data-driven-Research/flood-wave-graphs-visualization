from dataclasses import dataclass
from datetime import datetime


@dataclass
class GraphDataInterface:
    """
    Class for storing data preprocessed in a GraphDataHandler class.
    :param list graph_nodes: the nodes of the graph
    :param list graph_edges: the edges of the graph
    :param datetime min_date: the earliest node date on the graph
    :param list stations: the list of the stations on the graph
    :param dict positions: maps the nodes to their eventual positions on the
           grid
    """
    graph_nodes: list = None
    graph_edges: list = None
    min_date: datetime = None
    stations: list = None
    positions: dict = None
