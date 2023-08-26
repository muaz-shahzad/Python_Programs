import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1

ROWS = 3
COLS = 3

Symbol_Count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
Symbol_Value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_Wining(columns, lines, bet, Symbol_Val):
    winnings = 0
    wining_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # First column of the grid and take its values one by one
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += Symbol_Val[symbol] * bet
            wining_lines.append(line + 1)

    return winnings, wining_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  # cols = 3
        column = []
        current_Symbols = all_symbols[:]  # copy entire list
        for _ in range(rows):  # rows = 3
            value = random.choice(current_Symbols)  # choose random value from list
            current_Symbols.remove(value)  # Jo value choose ki h wo remove krdi  list m say
            column.append(value)  # usi value ko new list m append krdia column bnany k liye

        columns.append(column)  # ab us puri list jo k column h usy ek new list m add krdia final column generate
    return columns


def print_slot_machine(columns):
    # Here we are convert rows into coloumns
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])


def deposit():
    while True:
        try:
            amount = int(input("\nEnter Deposit Amount: $"))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("\nPlease Enter Number. ")
    return amount


def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"\nEnter Number of lines to bet on (1-" + str(MAX_LINES) + ")? "))
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        except ValueError:
            print("\nPlease Enter Number. ")
    return lines


def get_bet():
    while True:
        try:
            bet = int(input(f"\nEnter Amount for Bet on each line $(1-" + str(MAX_BET) + ")? "))
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\nBet Amount Range is ${MIN_BET} - ${MAX_BET}.")
        except ValueError:
            print("\nPlease Enter Amount in Digits. ")
    return bet


def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet_amount = get_bet()
        total_bet = bet_amount * lines
        if total_bet > balance:
            print(f"\nYou don't have sufficient balance for this bet. \nYour current balance is ${balance}")
        else:
            break
    print(f"\nYou are betting ${bet_amount} on ${lines} lines. \nTotal bet is equal to: ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, Symbol_Count)
    print("\n", slots)
    print_slot_machine(slots)
    print()
    winning, winning_lines = check_Wining(slots, lines, bet_amount, Symbol_Value)
    print(f"\nYou won ${winning}.")
    print(f"\nYou won on lines: ", *winning_lines)
    return winning - total_bet


def main():
    print("\nWelcome In Slot Machine Game")
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        play = input("\nPress Enter to Play (q to quit).")
        if play == "q":
            break
        else:
            balance += spin(balance)

    print(f"\nYou left with balance ${balance}")
    print("Good Bye..!!")


main()
