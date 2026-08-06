import pandas as pd
import pytest

from fwg_visualization.data.time_series_data_handler import (
    TimeSeriesDataHandler
)
from fwg_visualization.data.interfaces.time_series_data_interface import (
    TimeSeriesDataInterface
)


@pytest.fixture
def mock_year_range() -> tuple:
    """
    An example year range for which we will filter the data.
    :return tuple: the year range (first year and last year and everything
            in between will be included)
    """
    return '2000', '2004'


@pytest.fixture
def mock_yearly_data() -> dict:
    """
    Creates a mock data dictionary containing yearly data, on which we can
    test the code base.
    :return dict: the yearly mock data on which the tests will be run
    """
    mock_yearly_data: dict = {}
    mock_dates = pd.Index(
        data=['1999', '2000', '2001', '2002', '2003', '2004', '2005'],
        dtype='period[Y-DEC]',
        name='date'
    )

    mock_yearly_data[(300, 270)] = pd.DataFrame({
        'value': [14, 17, 6, 20, 22, 19, 3]
    }).set_index(mock_dates)

    mock_yearly_data[(220, 150)] = pd.DataFrame({
        'value': [1, None, 4, 31, 21, None, 11]
    }).set_index(mock_dates)

    mock_yearly_data[(120, 110)] = pd.DataFrame({
        'value': [9, 22, None, 21, 11, 4, 5]
    }).set_index(mock_dates)

    mock_yearly_data[(105, 40)] = pd.DataFrame({
        'value': [31, 29, 12, 21, 14, 11, 56]
    }).set_index(mock_dates)

    mock_yearly_data[(15, 2)] = pd.DataFrame({
        'value': [48, 26, 5, 13, 0, 43, 32]
    }).set_index(mock_dates)

    return mock_yearly_data


@pytest.fixture
def mock_quarterly_data() -> dict:
    """
    Creates a mock data dictionary containing quarterly data, on which we can
    test the code base.
    :return dict: the quarterly mock data on which the tests will be run
    """
    mock_quarterly_data: dict = {}
    mock_dates = pd.Index(
        data=['1999Q2', '1999Q3', '1999Q4',
              '2000Q1', '2000Q2', '2000Q3', '2000Q4',
              '2001Q1', '2001Q2', '2001Q3', '2001Q4',
              '2002Q1', '2002Q2', '2002Q3', '2002Q4',
              '2003Q1', '2003Q2', '2003Q3', '2003Q4',
              '2004Q1', '2004Q2', '2004Q3', '2004Q4',
              '2005Q1', '2005Q2'],
        dtype='period[Q-DEC]',
        name='date'
    )

    mock_quarterly_data[(300, 270)] = pd.DataFrame({
        'value': [42, 0, 87, 15, None, 63, 28, 91, 7, 54, 0, 39, 76, 18, 95,
                  None, 33, 61, 12, 84, 49, 0, 27, None, 70]
    }).set_index(mock_dates)

    mock_quarterly_data[(220, 150)] = pd.DataFrame({
        'value': [5, 19, None, 73, 44, 0, 82, 67, 11, 90, 36, 58, None, 24, 0,
                  99, 13, 46, 71, 8, None, 65, 32, 17, 0]
    }).set_index(mock_dates)

    mock_quarterly_data[(120, 110)] = pd.DataFrame({
        'value': [100, 94, 81, None, 22, 0, 57, 39, 68, 14, 75, 29, 0, None,
                  52, 86, 6, 41, 97, 18, 63, None, 34, 9, 0]
    }).set_index(mock_dates)

    mock_quarterly_data[(105, 40)] = pd.DataFrame({
        'value': [None, 26, 51, 78, 0, 13, 64, 88, 37, 20, 95, None, 4, 56,
                  72, 0, 31, 84, 16, 69, None, 45, 92, 8, 53]
    }).set_index(mock_dates)

    mock_quarterly_data[(15, 2)] = pd.DataFrame({
        'value': [17, 0, 62, 35, 89, None, 48, 23, 76, 10, 0, 54, 97, 41,
                  None, 66, 15, 83, 28, 0, 59, 94, None, 7, 38]
    }).set_index(mock_dates)

    return mock_quarterly_data


@pytest.fixture
def time_series_data_interface_y(
        mock_year_range: tuple,
        mock_yearly_data: dict) -> TimeSeriesDataInterface:
    """
    Preprocesses the received yearly data using a TimeSeriesDataHandler, which
    then stores this preprocessed data in a TimeSeriesDataInterface, which we
    will use for testing.
    :param tuple mock_year_range: the year range for which we filter the data
    :param dict mock_yearly_data: the yearly mock data on which we run the
           tests
    :return TimeSeriesDataInterface: the fixed data interface used for testing
    """
    time_series_data_handler_y = TimeSeriesDataHandler(
        year_range=mock_year_range,
        data=mock_yearly_data
    )
    time_series_data_handler_y.run()

    return time_series_data_handler_y.time_series_data_interface


@pytest.fixture
def time_series_data_interface_q(
        mock_year_range: tuple,
        mock_quarterly_data: dict) -> TimeSeriesDataInterface:
    """
    Preprocesses the received quarterly data using a TimeSeriesDataHandler,
    which then stores this preprocessed data in a TimeSeriesDataInterface,
    which we will use for testing.
    :param tuple mock_year_range: the year range for which we filter the data
    :param dict mock_quarterly_data: the quarterly mock data on which we run
           the tests
    :return TimeSeriesDataInterface: the fixed data interface used for testing
    """
    time_series_data_handler_q = TimeSeriesDataHandler(
        year_range=mock_year_range,
        data=mock_quarterly_data
    )
    time_series_data_handler_q.run()

    return time_series_data_handler_q.time_series_data_interface


@pytest.mark.parametrize('expected_station_pair_list', [
    [(300, 270), (220, 150), (120, 110), (105, 40), (15, 2)]
])
def test_station_pairs_y(
        time_series_data_interface_y: TimeSeriesDataInterface,
        expected_station_pair_list: list):
    """
    Tests whether the names of the station pairs in the created dictionary
    (contains yearly data) are as expected.
    :param time_series_data_interface_y: interface containing yearly data
    :param expected_station_pair_list: the expected list of the station pairs
    """
    station_pair_list = list(time_series_data_interface_y.statistics.keys())
    assert expected_station_pair_list == station_pair_list


@pytest.mark.parametrize('expected_data_frame_shape', [
    (5, 1)
])
def test_data_frame_shape_y(
        time_series_data_interface_y: TimeSeriesDataInterface,
        expected_data_frame_shape: list):
    """
    Tests whether the received yearly data was filtered to the correct size or
    not.
    :param time_series_data_interface_y: interface containing yearly data
    :param expected_data_frame_shape: the expected shape of the data frames
    """
    for data_frame in time_series_data_interface_y.statistics.values():
        assert data_frame.shape == expected_data_frame_shape


@pytest.mark.parametrize('expected_min_date, expected_max_date', [
    (pd.Period(value='2000', freq='Y'), pd.Period(value='2004', freq='Y'))
])
def test_data_filtering_y(
        time_series_data_interface_y: TimeSeriesDataInterface,
        expected_min_date: str,
        expected_max_date: str):
    """
    Tests whether the received yearly data was filtered correctly or not.
    :param time_series_data_interface_y: interface containing yearly data
    :param expected_min_date: the expected earliest year
    :param expected_max_date: the expected latest year
    """
    for data_frame in time_series_data_interface_y.statistics.values():
        assert min(data_frame.index) == expected_min_date
        assert max(data_frame.index) == expected_max_date


@pytest.mark.parametrize('expected_station_pair_list', [
    [(300, 270), (220, 150), (120, 110), (105, 40), (15, 2)]
])
def test_station_pairs_q(
        time_series_data_interface_q: TimeSeriesDataInterface,
        expected_station_pair_list: list):
    """
    Tests whether the names of the station pairs in the created dictionary
    (contains quarterly data) are as expected.
    :param time_series_data_interface_q: interface containing quarterly data
    :param expected_station_pair_list: the expected list of the station pairs
    """
    station_pair_list = list(time_series_data_interface_q.statistics.keys())
    assert expected_station_pair_list == station_pair_list


@pytest.mark.parametrize('expected_data_frame_shape', [
    (20, 1)
])
def test_data_frame_shape_q(
        time_series_data_interface_q: TimeSeriesDataInterface,
        expected_data_frame_shape: list):
    """
    Tests whether the received quarterly data was filtered to the correct size
    or not.
    :param time_series_data_interface_q: interface containing quarterly data
    :param expected_data_frame_shape: the expected shape of the data frames
    """
    for data_frame in time_series_data_interface_q.statistics.values():
        assert data_frame.shape == expected_data_frame_shape


@pytest.mark.parametrize('expected_min_date, expected_max_date', [
    (pd.Period(value='2000Q1', freq='Q'), pd.Period(value='2004Q4', freq='Q'))
])
def test_data_filtering_q(
        time_series_data_interface_q: TimeSeriesDataInterface,
        expected_min_date: str,
        expected_max_date: str):
    """
    Tests whether the received quarterly data was filtered correctly or not.
    :param time_series_data_interface_q: interface containing quarterly data
    :param expected_min_date: the expected earliest year
    :param expected_max_date: the expected latest year
    """
    for data_frame in time_series_data_interface_q.statistics.values():
        assert min(data_frame.index) == expected_min_date
        assert max(data_frame.index) == expected_max_date
