import pytest

from finanzen_base.Utils.date_ms import date_to_ms
from finanzen_base.Utils.date_ms import ms_to_date

date_ms_name = "date,ms"
date_ms = [("2020-01-01", 1577833200000),
           ("2021-07-12", 1626040800000),
           ("1970-01-01", -3600000)]


@pytest.mark.parametrize(date_ms_name,
                         date_ms
                         )
def test_date_to_ms(date, ms):
    assert date_to_ms(date) == ms


@pytest.mark.parametrize(date_ms_name,
                         date_ms
                         )
def test_ms_to_date(date, ms):
    assert ms_to_date(ms) == date


@pytest.mark.parametrize(date_ms_name,
                         date_ms
                         )
def test_inverse(date, ms):
    assert date == ms_to_date(date_to_ms(date))


def test_error():
    with pytest.raises(ValueError):
        assert date_to_ms("2020/01/02")
    with pytest.raises(TypeError):
        ms_to_date("1577833200000")
