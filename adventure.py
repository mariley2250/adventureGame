import time
import random
delayTime = 1
currentPosition = "field"
items = []


def printPause(text, delay):
    print(text)
    time.sleep(delay)


def checkItems(whichItem):
    if whichItem in items:
        return True
    else:
        return False


def decision(location):
    question = "What would you like to do?"
    locate = location
    if location == "field":
        printPause("Enter 1 to knock on the door of the house", delayTime)
        printPause("Enter 2 to peer into the cave", delayTime)
        selectionInput = input("What would you like to do?")
        if selectionInput == "1":
            house()
        elif selectionInput == "2":
            cave()
        else:
            selectionInput = ""
            printPause("Invalid Input", delayTime)
            decision(locate)
    elif location == "house":
        printPause("Enter 1 to fight the troll", delayTime)
        printPause("Enter 2 to runaway", delayTime)
        selectionInput = input(question)
        if selectionInput == "1":
            if checkItems("sword") is True:
                printPause("As the troll moves to attack, you unsheath your "
                           "new sword.", delayTime)
                printPause("The Sword of Ogoroth shines brightly in your "
                           "hand as you brace yourself for the attack.",
                           delayTime)
                printPause("But the troll takes one look at your shiny new "
                           "toy and runs away!", delayTime)
                printPause("You have rid the town of the troll. You are "
                           "victorious!", delayTime)
                endGame()
            else:
                printPause("You do your best...", delayTime)
                if random.randint(1, 2) == 2:
                    printPause("You inflict some damage to the troll but he "
                               "is only slightly hurt", delayTime)
                    printPause("The Troll pushes you back into the field and "
                               "it runs back inside the house", delayTime)
                    printPause("You need to find a better weapon", delayTime)
                    field()
                else:
                    printPause("but your dagger is no match for the dragon.",
                               delayTime)
                    printPause("You have been defeated!", delayTime)
                    endGame()
        elif selectionInput == "2":
            printPause("You run back into the field. Luckily, you don't seem"
                       " to have been followed.", delayTime)
            field()
        else:
            selectionInput = ""
            printPause("Invalid Input", delayTime)
            decision("house")


def intro():
    items.clear()
    printPause("You find yourself standing in an open field, filled with"
               " grass and yellow wildflowers.", delayTime)
    printPause("Rumor has it that a troll is somewhere around here, and has"
               " been terrifying the nearby village", delayTime)
    printPause("In your hand you hold your trusty (but not very effective)"
               " dagger.", delayTime)
    field()


def field():
    printPause("In front of you is a house.", delayTime)
    printPause("To your right is a dark cave", delayTime)
    decision("field")


def cave():
    printPause("You peer cautiously into the cave.", delayTime)
    printPause("It turns out to be only a very small cave.", delayTime)
    if checkItems("sword") is True:
        printPause("You've been here before, and gotten all the good stuff."
                   " It's just an empty cave now.", delayTime)
    else:
        printPause("Your eye catches a glint of metal behind a rock.",
                   delayTime)
        printPause("You have found the magical Sword of Ogoroth!", delayTime)
        printPause("You discard your silly old dagger and take the sword with"
                   " you.", delayTime)
        items.append("sword")
    printPause("You walk back out to the field.", delayTime)
    field()


def house():
    printPause("You approach the door of the house.", delayTime)
    printPause("You are about to knock when the door opens and out steps a"
               " troll.", delayTime)
    printPause("Eep! This is the troll's house!", delayTime)
    printPause("The troll attacks you!", delayTime)
    if checkItems("sword") is True:
        printPause("You arent bothered as your trusty sword with protect you.",
                   delayTime)
    else:
        printPause("You feel a bit under-prepared for this, what with only"
                   "having a tiny dagger.", delayTime)
    decision("house")


def endGame():
    selectionInput = input("Would you like to play again? (y/n)")
    if selectionInput == "y":
        printPause("Excellent! Restarting the game ...", delayTime)
        intro()
    elif selectionInput == "n":
        print("Thanks for playing, See you next time!")
    else:
        selectionInput = ""
        printPause("Invalid Input", delayTime)
        endGame()


intro()


# End Of Program
