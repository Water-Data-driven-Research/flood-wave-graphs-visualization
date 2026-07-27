from dataclasses import dataclass
from datetime import datetime


@dataclass
class GraphDataInterface:
    """
    Class for storing data preprocessed in a GraphDataHandler class.
    """
    data: dict = None
