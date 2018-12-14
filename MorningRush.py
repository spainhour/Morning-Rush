#####################
# Michael Spainhour #
# CSCI 150          #
# "Morning Rush"    #
# Final Project     #
#####################

import random
import re

class Character:

    def __init__(self, name, health, max_health):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.inventory = []
        self.position = None
        self.not_dead = True

    def is_alive(self):
        return self.health > 0

    def display_character(self):
        print "Health: " + "\t" + str(self.health)
        if self.health >= 3:
            print "Wellness: " + "\t" + "Feeling good"
        elif self.health == 2:
            print "Wellness: " + "\t" + "You've been better"
        elif self.health == 1:
            print "Wellness: " + "\t" + "You aren't in great shape"
        if self.inventory == []:
            print "Inventory:" + "\t" + "Empty"
        else:
            print "Inventory: " + str(self.inventory)
        print "\t"

class Room:

    def __init__(self, description, name):
        self.description = description
        self.name = name
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def display_items(self):
        if not self.is_empty():
            items_str = ""
            for i in self.items:
                items_str += str(i)
                print "You see " + items_str
        else:
            print "There are no items in this room."

def get_starting_room():

    Bedroom = Room("You are in the bedroom. Nothing too special here. There are doors " +\
                   "leading to the east and the south.", "Bedroom")

    MainCorridor = Room("You are in the main corridor. It is a long, dark hallway. " +\
                    "Doors lead to the north, south, and west.", "Main Corridor")

    Bathroom = Room("You are in the bathroom. It's surprisingly clean. To the north, you see " +\
                    "there is a door. A larger, more sturdy looking door is to the east. ", "Bathroom")

    Kitchen = Room("You are in the kitchen. You slept late this morning, and didn't get to breakfast " +\
                   "quick enough. There are two doors, one to the west and one to the north.", "Kitchen")

    Portal = Room("You have entered a portal to another dimension. Hmm. Nothing seems to be " +\
                  "too different from the other dimension. However, you can't explore this new dimension without the proper "
                      "authorization. A portal to the west will take you back home.", "Portal")

    Garage = Room("You are in the garage. A cabinet was left open. A door to the east will take you back to " +\
                  "the house.", "Garage")

    Bedroom_2 = Room("You've entered your brother's bedroom. The walls are littered " +\
                     "with inappropriate posters of women. There is a door to the south", "Brother's Bedroom")

    Bedroom.east = MainCorridor
    Bedroom.south = Kitchen
    MainCorridor.west = Bedroom
    MainCorridor.south = Bathroom
    Bathroom.north = MainCorridor
    Bathroom.east = Portal
    Kitchen.north = Bedroom
    Portal.west = Bathroom
    Kitchen.west = Garage
    Garage.east = Kitchen
    MainCorridor.north = Bedroom_2
    Bedroom_2.south = MainCorridor
    Bedroom_2.items.append("a game on a computer")
    Kitchen.items.append("a piece of cheese")
    Portal.items.append("your toothbrush!")
    Garage.items.append("a key")

    return Bedroom

def main():

    print "Welcome to Morning Rush! It's your task to explore the house, " +\
            "find your toothbrush, then make it back to your Bedroom and brush your " +\
            "teeth for school. Good luck!"
    print "\t"
    name = raw_input("What is your name? ")
    print "\t"
    print name + "," + " you awake from a glorious slumber. So glorious you've forgotten " +\
          "where you put your toothbrush. You must find it! Bad breath is not " +\
          "an option."
    print "\t"
    player_1 = Character(name, 7, 7)
    player_1.position = get_starting_room()
    victory = False

    while not victory and player_1.health > 0:
        player_1.display_character()
        print player_1.position.description
        player_1.position.display_items()

        user_input = raw_input("What would you like to do? ")
        take_cheese = re.findall(r"cheese", user_input)
        go_north = re.findall(r"north", user_input)
        go_east = re.findall(r"east", user_input)
        go_south = re.findall(r"south", user_input)
        go_west = re.findall(r"west", user_input)
        take_toothbrush = re.findall(r"toothbrush", user_input)
        take_key = re.findall(r"key", user_input)
        check_inventory = re.findall(r"inventory", user_input)
        play_game = re.findall(r"game", user_input)

        if go_north != []:
            if player_1.position.north != None:
                player_1.position = player_1.position.north
                if player_1.position.name == "Main Corridor":
                    num_answer = random.randint(1, 10)
                    num_guess = raw_input("Your older brother stands in your way. He says 'Pick a number between " +\
                          "1 and 10'. What is your guess? ")
                    if str(num_guess) == str(num_answer):
                        print "You can go free... This time."
                    else:
                        player_1.health -= 1
                        print "You guessed incorrectly so your brother punches you in the arm. " +\
                              "The correct answer was " + str(num_answer) + "."
                elif player_1.position.name == "Bedroom":
                    if "toothbrush" in player_1.inventory:
                        print "You made it back to your room with your toothbrush! " +\
                              "Gonna have some pearly whites all day! Congratulations!"
                        victory = True

            else:
                print "You can't go that way"
                print "\t"

        elif go_east != []:
            if player_1.position.east != None:
                player_1.position = player_1.position.east
                if player_1.position.name == "Main Corridor":
                    num_answer = random.randint(1, 10)
                    num_guess = raw_input("Your older brother stands in your way. He says 'Pick a number between " +\
                          "1 and 10'. ")
                    if str(num_guess) == str(num_answer):
                        print "You can go free... This time."
                    else:
                        player_1.health -= 1
                        print "You guessed incorrectly so your brother punches you in the arm. " +\
                              "The correct answer was " + str(num_answer) + "."
                elif player_1.position.name == "Portal":
                    print "The door is locked."
                    if "a key" in player_1.inventory:
                        print "You use your key to unlock the door."
                        player_1.position = player_1.position
                        player_1.inventory.remove("a key")
                    else:
                        player_1.position = player_1.position.west
                        print "You need a key to get through here."
            else:
                print "You can't go that way"
                print "\t"

        elif go_south != []:
            if player_1.position.south != None:
                player_1.position = player_1.position.south
            else:
                print "You can't go that way"
                print "\t"

        elif go_west != []:
            if player_1.position.west != None:
                player_1.position = player_1.position.west
                if player_1.position.name == "Bedroom":
                    if "toothbrush" in player_1.inventory:
                        print "You made it back to your room with your toothbrush! " +\
                              "Gonna have some pearly whites all day! Congratulations!"
                        victory = True
                    else:
                        "You still need to find your toothbrush!"
            else:
                print "You can't go that way."

        elif take_cheese != []:
            if player_1.position.name == "Kitchen":
                if player_1.position.items != []:
                    player_1.position.items = []
                    player_1.health -= 1
                    print "You take the cheese and smell it. It smells pretty bad, but it's just " +\
                          "cheese. You take one bite and throw up... That wasn't a great idea."
                else:
                    print "There is no cheese."
            else:
                print "Invalid Input"

        elif take_toothbrush != []:
            if player_1.position.name == "Portal":
                if "toothbrush" not in player_1.inventory:
                    print "You pick up your toothbrush and put it in your pocket."
                    player_1.position.items = []
                    player_1.inventory.append("toothbrush")
                else:
                    print "You already have your toothbrush."
            else:
                print "Invalid Input"

        elif take_key != []:
            if player_1.position.name == "Garage":
                if "a key" not in player_1.inventory:
                    print "You inspect the key. This might come in handy later so you put " +\
                          "it in your pocket."
                    player_1.position.items = []
                    player_1.inventory.append("a key")
                else:
                    print "You already have a key"
            else:
                print "Invalid Input"

        elif play_game != []:
            if player_1.position.name == "Brother's Bedroom":
                print "\t"
                print "This is the 'Guess My Number Game'. I have a number " +\
                      "between 1 and 100, you need to guess it quickly. " +\
                      "I will give you feedback: HIGH, LOW or CORRECT. " +\
                      "Guess until you get the number correct. Good Luck!"

                r = int(random.random() * 100) + 1
                guess = int(raw_input("What is your guess? "))
                while guess != r:
                        if guess < r:
                            print "LOW"
                        else:
                            print "HIGH"
                        guess = int(raw_input("What is your guess? "))
                print "CORRECT"
                print "You back away from the computer"

            else:
                "Invalid Input"
        else:
            print "Invalid Input"

        print "\t"

    if player_1.health == 0:
        print "Ouch. You took quite the beating. You should just go lay back down."
        print "Game Over"


main()
