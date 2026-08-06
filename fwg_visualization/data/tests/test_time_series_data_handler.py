from datetime import datetime

import pandas as pd
import pytest

from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)
from fwg_visualization.data.time_series_data_handler import (
    TimeSeriesDataHandler
)


@pytest.fixture
def mock_data() -> dict:
    """
    Creates a mock data dictionary on which we can test the code base.
    :return dict: the mock data on which the tests will be run
    """
    mock_data: dict = {}
    mock_station_pairs = [(300, 270), (220, 150), (120, 110), (105, 40),
                          (15, 2)]
    mock_dates = pd.Index(
        data=['1999', '2000', '2001', '2002', '2003', '2004', '2005'],
        dtype='period[Y-DEC]',
        name='date'
    )

    mock_data[(300, 270)] = pd.DataFrame({
        'value': [14, 17, 6, 20, 22, 19, 3]
    }).set_index(mock_dates)

    mock_data[(220, 150)] = pd.DataFrame({
        'value': [1, None, 4, 31, 21, None, 11]
    }).set_index(mock_dates)

    mock_data[(120, 110)] = pd.DataFrame({
        'value': [9, 22, None, 21, 11, 4, 5]
    }).set_index(mock_dates)

    mock_data[(105, 40)] = pd.DataFrame({
        'value': [31, 29, 12, 21, 14, 11, 56]
    }).set_index(mock_dates)

    mock_data[(15, 2)] = pd.DataFrame({
        'value': [48, 26, 5, 13, 0, 43, 32]
    }).set_index(mock_dates)

    return mock_data

