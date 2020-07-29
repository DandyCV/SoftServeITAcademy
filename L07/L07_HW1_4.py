def season(month):
    """Returns - string (season of year).
     Argument - integer from 1 to 12 (number of month)."""
    if 0 < month < 3 or month == 12: return "Winter"
    if 2 < month < 6: return "Spring"
    if 5 < month < 9: return "Summer"
    if 8 < month < 12: return "Autumn"


print(season(7))