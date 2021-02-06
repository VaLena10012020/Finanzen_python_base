import time
from datetime import datetime


def date_to_ms(date: str):
    return int(time.mktime(time.strptime(date, "%Y-%m-%d")) * 1000)


def ms_to_date(ms: int):
    return str(datetime.fromtimestamp(ms/1000.0).date())
