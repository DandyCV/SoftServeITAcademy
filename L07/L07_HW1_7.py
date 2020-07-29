def date(day, month, year):
    """Takes 3 int arguments: day, mont, year.
    Returns True if date is in calendar and False if not."""
    in_calendar = False
    if year > 0:
        if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
            in_calendar = True
        elif month in [4, 6, 9, 11] and 0 < day < 31:
            in_calendar = True
        elif month == 2:
            if year % 4 and 0 < day < 29 or not year % 4 and 0 < day < 30:
                in_calendar = True
    return in_calendar


def main():
    user_dater = input("Enter the date in format [dd.mm.yy]: ").split(".")
    print("Date is in calendar?", date(int(user_dater[0]), int(user_dater[1]), int(user_dater[2])))


if __name__ == '__main__':
    main()
