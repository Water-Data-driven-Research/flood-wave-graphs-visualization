from dataclasses import dataclass


@dataclass
class AxisDataInterface:
    """
    Class for storing data calculated in an AxisDataCalculator class.
    :param list x_ticks: the ticks on the x-axis
    :param list x_tick_labels: the labels of the ticks on the x-axis
    :param list y_ticks: the ticks on the y-axis
    :param list y_tick_labels: the labels of the ticks on the y-axis
    """
    x_ticks: list = None
    x_tick_labels: list = None
    y_ticks: list = None
    y_tick_labels: list = None
