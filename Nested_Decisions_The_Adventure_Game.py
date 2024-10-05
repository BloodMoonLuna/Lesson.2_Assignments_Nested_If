# Task 1: You are provided with a Python script that is supposed to guide a user throough an adventure game, but it has some errors. Identify and fix them.
#Task 2: Based on your correction from Task 1, expand the game. If the user chosses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide an outcome for each.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("Do you want to light a torch, or continue in the dark? ")
    if action == "light a torch":
        print("You light a torch, and find treasure in the back of the cave!")
    else:
        print("You stumble around in the dark. You trip and fall, scrapping your knee.")
