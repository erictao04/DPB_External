import datetime


def dt_to_str(date):
    date = datetime.date.strftime(date, "%Y-%m-%d")
    return date


def str_to_dt(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date


def n_decim(price):
    decimal_length = 2
    decimal_length = 3 if price < 100 else decimal_length
    decimal_length = 4 if price < 10 else decimal_length
    decimal_length = 5 if price < 1 else decimal_length
    decimal_length = 6 if price < .5 else decimal_length

    return round(price, decimal_length)


def two_decim(price):
    return round(price, 2)
