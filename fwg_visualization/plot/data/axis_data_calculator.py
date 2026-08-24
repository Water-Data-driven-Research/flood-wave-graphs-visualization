from datetime import timedelta

from fwg_visualization.data.interfaces.graph_data_interface import (
    GraphDataInterface
)
from fwg_visualization.plot.data.interfaces.axis_data_interface import (
    AxisDataInterface
)


class AxisDataCalculator:
    """
    Calculates the data to be put on the x- and y-axes that will be displayed
    on the figure.
    """
    def __init__(self, graph_data_if: GraphDataInterface):
        """
        Constructor.
        :param GraphDataInterface graph_data_if: contains data about the graph
        """
        self.min_date = graph_data_if.min_date
        self.stations = graph_data_if.stations
        self.positions = graph_data_if.positions

        self.data_if = AxisDataInterface()

    def run(self):
        """
        Run function, calculates the required axis data (the ticks and the tick
        labels of the x- and y-axes) and stores it in the AxisDataInterface
        instance.
        """
        x_coordinates = [pos[0] for pos in self.positions.values()]

        min_x = min(x_coordinates)
        max_x = max(x_coordinates)

        no_of_ticks = min(max_x - min_x, 20)
        self.data_if.x_ticks = list(range(
            int(min_x),
            int(max_x) + int(max_x / no_of_ticks),
            int(max_x / no_of_ticks)
        ))
        self.data_if.x_tick_labels = [
            (self.min_date + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in self.data_if.x_ticks
        ]

        self.data_if.y_ticks = list(range(len(self.stations)))
        self.data_if.y_tick_labels = self.stations
