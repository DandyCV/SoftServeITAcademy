def arithmetic(value_1, value_2, operation):
    """Function makes mathematical operations with 2 numbers.
    First and second arguments - int/float numbers
    Third argument - string operator(+, -, *, /)"""
    if operation == "+": return value_1 + value_2
    if operation == "-": return value_1 - value_2
    if operation == "*": return value_1 * value_2
    if operation == "/": return value_1 / value_2
    return "Unknown operation"


print(arithmetic(12, 3, "*"))
