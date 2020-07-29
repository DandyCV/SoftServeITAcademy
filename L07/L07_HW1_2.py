def is_year_leap(year):
    """Function check if year is leap.
    Argument - integer (year)."""
    not_leap = year % 4
    if not_leap: 
        return False
    return True


print(is_year_leap(2001))
