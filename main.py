# Dice rolling game

# import random
#
# is_running = True
#
# while is_running:
#
#     choice = input("Roll the dice? (y/n): ")
#
#     if choice.lower() != 'y' and choice.lower() != 'n':
#         print("Invalid choice!")
#
#     if choice.lower() == 'y':
#         print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
#     elif choice.lower() == 'n':
#         print("Tanks for playing!")
#         is_running = False

###########################################################################

import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif choice == 'n':
        print("Tanks for playing!")
        break
    else:
        print("Invalid choice!")