def is_prime(number):
    """Returns True if number is prime. And False if not.
    Takes 1 argument - positive integer"""
    if number > 3:
        for num in range(2, number):
            if not number % num:
                return False
    return True


def main():
    user_number = int(input("Enter the number: "))
    print("%d is prime?" % user_number, is_prime(user_number))


if __name__ == "__main__":
    main()
