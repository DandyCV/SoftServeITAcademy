def bank(n, years):
    """Function count the sum of your bank deposit with 10% per year.
    Takes 2 integer arguments: float[sum of money], int[number of years].
    Return int[sum of deposit in the end]"""
    for year in range(years):
        n *= 1.1
    return round(n, 2)


def main():
    user_sum = float(input("Enter the sum of deposit: "))
    user_years = int(input("Enter the period length: "))
    print("Total sum in %d year(s): %.2f" %(user_years, bank(user_sum, user_years)))


if __name__ == "__main__":
    main()
