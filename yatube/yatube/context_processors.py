import datetime as dt


def determines_the_current_year(request):
    now_year = dt.datetime.now()
    now_year = now_year.year
    return {'determines_the_current_year': now_year}
