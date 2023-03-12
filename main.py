from art import logo
from game_data import data
import random

GAME_ON = True
print(logo)
print("Welcome to the Higher Lower")


def compare_a():
    i = random.randint(0, len(data)) - 1
    name_a = data[i]["name"]
    flw_a = int(data[i]["follower_count"])
    dscp_a = data[i]["description"]
    country_a = data[i]["country"]
    print_a = f"\nCompare A : {name_a} a {dscp_a} from {country_a} "
    return flw_a, print_a


def compare_b():
    i = random.randint(0, len(data)) - 1
    name_b = data[i]["name"]
    flw_b = int(data[i]["follower_count"])
    dscp_b = data[i]["description"]
    country_b = data[i]["country"]
    print_b = f"\nCompare B : {name_b} a {dscp_b} from {country_b} "
    return flw_b, print_b


def main():
    flw_a, print_a = compare_a()
    flw_b, print_b = compare_b()
    again = True
    print(print_a)
    print(print_b)
    answer = input("\nWhich is higher A or B?\n").lower()
    if answer == "a" and flw_a >= flw_b:
        print(f"\nYou are correct {flw_a}k > {flw_b}k.\n")
    elif answer == "b" and flw_b >= flw_a:
        print(f"\nYou are correct {flw_b}k > {flw_a}k.\n")
    else:
        again = input(
            f"You lost {flw_a}k to {flw_b}k\nYou wanna play again? Y or N\n"
        ).lower()
        global GAME_ON
        GAME_ON = False
    return again


play_again = main()

if play_again == "y":
    GAME_ON = True
while GAME_ON:
    main()
