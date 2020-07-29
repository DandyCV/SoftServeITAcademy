def square(size):
    """Function returns tuple with float {[perimeter], [area], [diagonal]}
    Argument - integer/float (side of square)"""
    perimeter = 4 * size
    area = size ** 2
    diagonal = round((2 * area) ** 0.5, 2)
    square_tuple = (perimeter, area, diagonal)
    return square_tuple


print(square(3))
