from datetime import datetime


def date_to_ms(date: str):
    return datetime.strptime(date, "%Y-%m-%d").timestamp()*1000


def ms_to_date(ms: int):
    return str(datetime.fromtimestamp(ms/1000.0).date())
