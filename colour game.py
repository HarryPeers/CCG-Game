from random import choice
from time import sleep
from os import system

colours = {
    1: "red",
    2: "yellow",
    3: "green",
    4: "blue",
    5: "white"
}

def clear_console():
    system("cls")

def start_menu(computer, person):
    menu = f"Computer score: {computer}, Player score: {person}\n"
    menu += "-"*(len(menu)-1)+"\n"
    return menu

while True:
    current_console = start_menu(0, 0)
    computer_score = 0
    player_score = 0
    for x in range(1):
        current_console = start_menu(computer_score, player_score)
        current_console += "Please select a colour from below..."
        print(current_console)
        current_console += "\n"

        for key in colours.keys():
            print(f"    {key}: {colours[key]}")
            current_console += f"    {key}: {colours[key]}\u001b[0m\n"

        while True:
            try:
                player_choice = int(input())
                if player_choice <= 0 or player_choice >= 6:
                    raise
            except:
                print("That is not a valid choice!")
                current_console += "That is not a valid choice!\n"
            else:
                break

        player_colour = colours[player_choice]
        computer_colour = choice(list(colours.values()))

        current_console += "Your guess was"
        clear_console()
        print(current_console)
        sleep(0.5)
        clear_console()
        current_console += "."
        print(current_console)
        sleep(0.5)
        clear_console()
        current_console += "."
        print(current_console)
        sleep(0.5)
        clear_console()
        current_console += "."
        print(current_console)
        sleep(0.5)

        if player_colour == computer_colour:
            player_score += 1
            current_console += f" \u001b[32mcorrect!\u001b[0m\nYou have gained 1 point!"
        else:
            computer_score += 1
            current_console += f" \u001b[31mincorrect!\u001b[0m\nThe computer has gained 1 point!"
        clear_console()
        print(current_console)
        sleep(3)
        clear_console()
        current_console = ""
    clear_console()
    if computer_score > player_score:
        print("The computer won! Would you like to play again?")
    else:
        print("You won! Would you like to play again?")
    o = input()
    if o.lower() in ["n", "no", "f", "false"]:
        break
    clear_console()
