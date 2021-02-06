from datetime import datetime, timezone


def date_to_ms(date_str: str, date_split: str = "-") -> int:
    date_list = date_str.split(date_split)
    date_obj = datetime(int(date_list[0]),
                        int(date_list[1]),
                        int(date_list[2]), tzinfo=timezone.utc)
    return int(date_obj.timestamp() * 1000)


def ms_to_date(ms: int) -> str:
    return str(datetime.utcfromtimestamp(ms/1000.0).date())
