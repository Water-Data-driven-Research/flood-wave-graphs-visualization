from datetime import timedelta

import numpy as np
import pandas as pd

from fwg_visualization.plot.delta_peak_plotter.interfaces. \
    delta_peak_data_interface import DeltaPeakDataInterface


class DeltaPeakDataHandler:
    """
    This class prepares the data for visualizing delta peaks.
    """
    def __init__(self,
                 time_series: pd.DataFrame,
                 peak_dates: pd.DatetimeIndex,
                 null_point: int,
                 delta: int):
        """
        Constructor.
        :param pd.DataFrame time_series: the received time series data
        :param pd.DatetimeIndex peak_dates: list of the dates of the delta
               peaks
        :param int null_point: the null point of the station
        :param int delta: the delta value
        """
        self.time_series = time_series
        self.peak_dates = peak_dates
        self.null_point = null_point

        self.data_if = DeltaPeakDataInterface(delta=delta)

    def run(self, date_range: dict):
        """
        Run function, filters, null corrects, and prepares the data for
        plotting.
        :param dict date_range: the given date range
        """
        new_date_range = self.calculate_new_date_range(date_range=date_range)

        desired_points = self.time_series.loc[
            new_date_range['start']:new_date_range['end']
        ]

        self.data_if.data_points = desired_points.replace(
            to_replace=desired_points.array,
            value=np.round(a=(desired_points.array / 100 + self.null_point),
                           decimals=4)
        )

        self.data_if.delta_peaks = self.data_if.data_points[
            self.data_if.data_points.index.isin(self.peak_dates.astype('str'))
        ]

    def calculate_new_date_range(self, date_range: dict) -> dict:
        """
        Calculates a new date range based on where the delta peaks are.
        :param dict date_range: the given date range
        :return dict: the updated date range (based on the delta peaks)
        """
        points_within_range = self.time_series.loc[
            date_range['start']:date_range['end']
        ]

        points_within_range.index = pd.to_datetime(
            points_within_range.index
        )

        delta_peaks = points_within_range[
            points_within_range.index.isin(self.peak_dates)
        ]

        new_date_range = {
            'start': (delta_peaks.index[0]
                      - timedelta(days=self.data_if.delta + 2)
                      ).strftime(format='%Y-%m-%d'),
            'end': (delta_peaks.index[-1]
                    + timedelta(days=self.data_if.delta + 2)
                    ).strftime(format='%Y-%m-%d')
        }

        return new_date_range
