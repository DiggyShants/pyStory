import sys
import time

short = 0.08
medium = 0.02
long = 2

def ending():
    print()
    print("The screen flashes off and a beam of light from above surrounds you.")
    time.sleep(long)
    print("All you can see is a soft white light. It feels like you are weightless.")
    time.sleep(long)
    print("You are not sure what is left, but you know you have exited the loop.")
    time.sleep(long)
    print()
    print("GAME OVER")
    print("Thanks for playing.")

def door1_1():
    print()
    print("The staircase gets dimmer as you go down.")
    time.sleep(long)
    print('"Welcome to the end of the loop," a monotone voice speaks.')
    time.sleep(long)
    print("You see a face on a screen on the far side.")
    time.sleep(long)
    print('"I am the ship\'s AI. Please enter the boolean value below."')
    time.sleep(long)
    print("There is a keyboard right below the talking face.")
    time.sleep(long)
    print()
    bool = input("What do you enter?: ").lower().strip()
    if bool == "false":
        ending()
    else:
        print("A bright light flashes and then everything goes black.")
        time.sleep(long)
        intro()

def door1_2():
    print()
    print("Eeeeeeeeeee! There is a high pitched squeal and the floor drops out from under you.")
    time.sleep(long)
    print("You find yourself sliding down a metal ramp.")
    time.sleep(long)
    print("lights flash past you as you descend rapidly")
    time.sleep(long)
    print("You roll into the room and a door seals you off from the ramp.")
    time.sleep(long)
    print("You are in a small circular room.")
    time.sleep(long)
    print("You can barely make out the number FF6633 printed on the wall.")
    time.sleep(long)
    print("There is a door with three buttons. The buttons light up a dim orange, blue and red.")
    time.sleep(long)
    print()
    color = input("Which button do you press?(orange/blue/red): ").lower().strip()
    if color == "orange":
        print()
        door1_1()
    else:
        print()
        print("A bright orange light flashes and then everything goes black.")
        intro()

def door2_1():
    print()
    print("You find your self on a platform darkness stretches out in all directions.")
    time.sleep(long)
    print("There are two staircases headed down off the platform.")
    time.sleep(long)
    print("There are two shapes next to the staircases.")
    time.sleep(long)
    print("There is an oval on the left staircase and a parallelogram on the right staircase.")
    time.sleep(long)
    print()
    staircase = input("Which staircase do you descend?(left/right): ").lower().strip()
    if staircase == "left":
        door1_1()
    else:
        print()
        print("A bright light flashes and then everything goes black.")
        time.sleep(long)
        intro()

def door2_2():
    print()
    print("You are in yellowish room.")
    time.sleep(long)
    print("There is a hallway that splits into two directions.")
    time.sleep(long)
    print("To the east you can hear some water flowing.")
    time.sleep(long)
    print("To the west, there seems to be some beeping noises.")
    time.sleep(long)
    print()
    path = input("Which hallway do you go down?(east/west): ").lower().strip()
    if path == "west":
        print("You wander down the dim hallway.")
        time.sleep(long)
        print("The beeping noises fades away.")
        time.sleep(long)
        door1_2()
    else:
        print()
        print("A bright light flashes and then everything goes black.")
        time.sleep(medium)
        intro()

def door3_1():
    print()
    print("You walk into a room with greenish metal walls.")
    time.sleep(long)
    print("The room is a rectangle shape about 8 square meters.")
    time.sleep(long)
    print('"Do you want my help?" the monotone voce asks.')
    time.sleep(long)
    print()
    answer = input("How do you respond?(yes/no): ").lower().strip()
    if answer == "yes" or answer == "y":
        print('"Close your eyes!" the voice commands.')
        time.sleep(long)
        print("You close your eyes and when you open them you are somewhere else.")
        time.sleep(medium)
        door2_2()
    else:
        print()
        print("A bright light flashes and then everything goes black.")
        time.sleep(medium)
        intro()



def door3_2():
    print()
    print("You walk into a room with no lights, everything is dark.")
    time.sleep(long)
    print("You feel around with your hands and your hands find a sharp wire on the floor.")
    time.sleep(long)
    print("A bright light flashes and then everything goes black.")
    time.sleep(medium)
    intro()

def door1():
    print()
    print("You walk down a long corridor. You bare feet feel cold on the metal floor.")
    time.sleep(long)
    print("There is a faint red light glowing from a strip of lights that runs the entire hallway.")
    time.sleep(long)
    print("You notice the walls are decorated with repeating 0 and 1 combinations.")
    time.sleep(long)
    print("You see 1101010100 printed on the left hand wall.")
    time.sleep(long)
    print("At the end of the hallway there is a key pad.")
    print()
    time.sleep(long)
    keypad = input("Which number do you want to enter?: ").strip()
    if keypad == 852:
        print()
        print("The door slides open and reveals a staircase down.")
        door1_1()
    else:
        door1_2()


def door2():
    print()
    print("You enter a circular room.")
    time.sleep(long)
    print("There a a white light coming from the ceiling.")
    time.sleep(long)
    print("There is a small window that gives you a view of space.")
    time.sleep(long)
    print('"Where am I?" you think to yourself.')
    time.sleep(long)
    print("There are two doors that exit the room.")
    time.sleep(long)
    print(" One door is painted orange and the other is painted blue.")
    time.sleep(long)
    print()
    door = input("Which door do you want to enter?(orange/blue): ").lower().strip()
    if door == "orange":
        door2_1()
    else:
        door2_2()

def door3():
    print()
    print("You go through the door and you are standing on glass above water.")
    time.sleep(long)
    print("There is a blue glow all over the room.")
    time.sleep(long)
    print('There are two open archways. One heads to the left and one heads to the right.')
    time.sleep(long)
    print('"Hello again," booms a monotone voice.')
    time.sleep(long)
    print('"We have met here so many times," the voice continues.')
    time.sleep(long)
    print('"If you want to break out, look for the complimentary color of blue." ')
    time.sleep(long)
    direction = input("Which direction do you want to go in?(left/right): ").lower().strip()
    if direction == "left":
        print()
        door3_1()
    else:
        print()
        print("A bright light flashes and then everything goes black.")
        door3_2()

def askForPath():
    firstPath = input("Which door do you go through? (1/2/3): ").lower().strip()
    if firstPath == "1":
        print()
        door1()
    elif firstPath == "2":
        print()
        door2()
    elif firstPath == "3":
        print()
        door3()
    else:
        print("Please enter 1, 2, or 3")
        askForPath()

def intro():
    print()
    print("Everything is dark. You feel around with your hands.")
    time.sleep(long)
    print("Your hands feel cold metal beneath you.")
    time.sleep(long)
    print("You stand up and walk to a wall.")
    time.sleep(long)
    print("CLICK!")
    print("Your hand presses a button and light fills the room.")
    time.sleep(long)
    print("You are in a small metal room with four walls.")
    time.sleep(long)
    print("Three of the walls seem to have doors with a button to open them.")
    time.sleep(long)
    print("Door 1: This door is on your left. There is a red light above it.")
    print("Door 2: This door is straight ahead. There is a green light above it.")
    print("Door 3: This door is on your right. There is a blue light above it.")
    print()
    time.sleep(long)
    askForPath()



print("###########################")
print("#                         #")
print("#     While True Loop     #")
print("#                         #")
print("###########################")
print()
time.sleep(long)
print("Wha...What happened? Where am I?")
time.sleep(long)
print("Everything is dark. It is silent.")
time.sleep(long)
print("You look at your hands. They have small cuts on them.")
time.sleep(long)
print("Carved into your wrist are the numbers 255, 125, 0")
time.sleep(long)
print()
startGame = input("Would you link to play the story? (yes/no): ").lower().strip()

if startGame == "yes" or startGame == "y":
    intro()
else:
    print("That's too bad.")

