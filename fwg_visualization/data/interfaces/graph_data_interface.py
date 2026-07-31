from dataclasses import dataclass
from datetime import datetime


@dataclass
class GraphDataInterface:
    """
    Class for storing data preprocessed in a GraphDataHandler class.
    :param datetime min_date: the earliest node date on the graph
    :param list stations: the list of the stations on the graph
    :param dict pos: maps the nodes to their eventual positions on the grid
    """
    min_date: datetime = None
    stations: list = None
    pos: dict = None
