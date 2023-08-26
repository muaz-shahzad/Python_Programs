import random

Symbol_Count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

Symbol_Val = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
rows = 3
cols = 3

all_symbols = []
for symbol, symbol_count in Symbol_Count.items():
    for _ in range(symbol_count):
        all_symbols.append(symbol)

print("\n", all_symbols)
columns = []
for _ in range(cols):  # cols = 3
    print(f"\nProgram Run For Cols {_}")
    column = []
    print("Main Columns List", columns)
    print("Loop Single Column ", column)
    current_Symbols = all_symbols[:]  # copy entire list
    print("Copied List ", current_Symbols)
    for _ in range(rows):  # rows = 3
        print(f"\nProgram Run For Rows {_}")
        value = random.choice(current_Symbols)  # choose random value from list
        print("Random Value Selected From Copied List  ", value)
        current_Symbols.remove(value)  # Jo value choose ki h wo remove krdi  list m say
        print("Copied List After Remove Selected Random Value Remove", current_Symbols)
        column.append(value)  # usi value ko new list m append krdia column bnany k liye
        print("Loop Single Column List ", column)

    columns.append(column)  # ab us puri list jo k column h usy ek new list m add krdia final column generate
    print("\nLoop Single Column Append Main Columns List ", columns)

print("\nLength", len(columns))



print("\n")
for row in range(len(columns[0])):
    for i, column in enumerate(columns):
        if i != len(columns) - 1:
            print(column[row], "|", end=" ")
        else:
            print(column[row])


print("\n")

for i, column in enumerate(columns):
    print(i, column)


lines = 3
bet = 50
print("\n Winning")
winnings = 0
wining_lines = []
for line in range(lines):
    print(f"\nProgram Run For Line {line}")
    symbol = columns[0][line]
    print("Column 0", columns[0])
    print("Symbol ", symbol)
    for column in columns:
        print("Columns " , column)
        symbol_check = column[line]
        print("Symbol Check = " , symbol_check)
        if symbol != symbol_check:
            break
        else:
            print("\nWining Before =>" ,winnings)
            winnings += Symbol_Val[symbol] * bet
            print("Wining After =>" ,winnings)
            wining_lines.append(line + 1)
            print("Wining Lines=> " , wining_lines)

print("\n")
print("\n")
print("\n")
print("\n")

for line in range(lines):
    print(f"Lines is {line}")
    for column in columns:
        print(f"Column is {column}")
        print(f"Column[line] is {column[line]}")








