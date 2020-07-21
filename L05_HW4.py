#прямокутник із символів
outline_symbol = input("Enter outline symbol: ")
inline_symbol = input("Enter inline symbol: ")
width = int(input("Enter the width of rectangle: "))
height = int(input("Enter the height of rectangle: "))
print(outline_symbol * width)
for line in range(height):
    print(outline_symbol + inline_symbol * (width - 2) + outline_symbol)
print(outline_symbol * width)

