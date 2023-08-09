import random


# 1 Water
# 2 Snake
# 3 Gun

def check(computer, player):
    if computer == player:
        return 0
    if computer == 1 and player == 3:
        return -1
    if computer == 2 and player == 1:
        return -1
    if computer == 3 and player == 2:
        return -1
    return 1


print("\nWelcome to (Snake Water Gun) Game ")
computer = random.randint(1, 3)
print("\n1 Water \n2 Snake \n3 Gun")
player = int(input("Select Your Option (1-3): "))

score = check(computer, player)
if score == 0:
    print("\nMatch Draw")
elif score == -1:
    print("\nYou Loss ")
else:
    print("\nYou Won")
