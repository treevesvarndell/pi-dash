from datetime import datetime, timedelta


def datetime_now():
    return datetime.now()


def datetime_plus(minutes=0, hours=0):
    return datetime_now() + timedelta(minutes=minutes, hours=hours)