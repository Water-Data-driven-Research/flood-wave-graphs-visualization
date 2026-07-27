from dataclasses import dataclass
from datetime import datetime


@dataclass
class GraphDataInterface:
    """
    Class for storing data preprocessed in a GraphDataHandler class.
    :param dict data: the data to be stored
    """
    data: dict = None
