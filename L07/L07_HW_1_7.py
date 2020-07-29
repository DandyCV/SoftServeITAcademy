def date(day, month, year):
    """Takes 3 int arguments: day, mont, year.
    Returns True if date is in calendar and False if not."""
    in_calendar = False
    if year > 0:
        if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
            in_calendar = True
        elif month in [4, 6, 9, 11] and 0 < day < 31:
            in_calendar = True
        elif month == 2 



