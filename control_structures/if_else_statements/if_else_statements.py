# Using if / else Statements, Ryan Kelley, February 05, 2020.  Version 0.4


import random # This is a special library built-in to Python.  It has special methods, in this case .shuffle() that I will use in this code. 
import time # This lets us call the sleep() method which pauses the program for a specified number of seconds.
print("*###############################################################*")
print("[            Working with if / else Statements $Version 0.4$    ]")
print("[                              by                               ]")
print("[                          Ryan Kelley                          ]")
print("[                      February 05, 2020                        ]")
print("[                                                               ]")
print("[                                                               ]")
print("*###############################################################*")
print("Hello $user, this program will help you learn how to use if / else statements in your code.  If you have any questions while using this program please raise your hand.  The human lifeform in charge of class can assist you.\n")
print("$user, I hope you think I am a useful program.  I will pause at times so you can read my output.  You can change how long I will pause.\n")
time.sleep(2)
wait_time = input("How many seconds should I pause $user?  Please enter a whole number and press [ENTER].  You cannot change this without restarting the program.\n")
wait_time = int(wait_time)
print("Ok $user, when I pause I will do so for",wait_time,"seconds.\n")
user0 = str(input("$user, by what name should I call you?  Please, type your firt and last name and then press ENTER on your keyboard.\n")) # Create a variable named user and assign it a value.
# In Python, = is the English equivalent of "Make the thing on the left have the same value as the thing on the right."  
print("Give me a second to write that down...\n")
time.sleep(wait_time) # Pause.

# The following lines of code create three slices of the user name and then rearranges them.  Remember you start counting at 0! 
user1 = user0[0:2] # 1st-3rd Letters
user2 = user0[2:5] # 3rd-6th Letters
user3 = user0[5:len(user0)] # 6th-Last Letters
user4 = user3 + user2 + user1

print("Hello,",user4,"!  It is so nice to meet a new user.  I will do my best to be a good program.\n")
name_correct = input("Is this really what I should call you?  [Type Yes or No, then press ENTER.]\n") # Create the variable name_correct and assign it a value. 
name_correct = name_correct[0] # This assigns the name_correct variable to JUST the first letter of the user's answer. 
name_correct = str.lower(name_correct) # This assigns the name_correct variable to the lower case version of that first letter.
print("I am so terribly sorry.  My memory banks are full.  Give me a second to store this data.\n")
time.sleep(wait_time) # Pause. 


# Our first if / else statement starts here.  It will check the VALUE of the name_correct variable and then test it against each CONDITION.

if name_correct == "y": # == is the English equivalent of "Is the thing on the left the same as the thing on the right?"
    # If they answer yes just leave user0 variable alone and continue on in the program.
    print("Ok, ",user0,"it is!\n")
elif name_correct == "n":
    # On the next line we will have the user re-type their name.  
    user0 = str(input("I am sorry.  I experienced a memory error.  I might have a bug.  Please type your name and press enter.\n"))
    print("Ahh! Yes,",user0,"that's more like it!\n")
else:
    x = 5
    while x != 0:
        print("Please enter Yes or No only.  Something has caught fire.  Emergency!  Prepare for program crash in",x,"seconds\n")
        time.sleep(1)
        x += -1
    exit()

time.sleep(wait_time) # Pause.

print(user0,"it's time to move on!  For the next part of this program you will roll a six-sided die to simulate random number generation.  If you don't have a die, please raise your hand.\n")
dice_roll = int(input("Please roll the die one time.  Type the number you rolled and press enter.\n"))

# Our second if / else statement.  This checks for each number possible on the die roll. 

if dice_roll == 1:
    print("So much fun, you rolled a one!\n")
    print("Please ask for a Blue Raspberry Jolly Rancher.\n") 
elif dice_roll == 2:
    print("Good for you, it's a two!\n")
    print("Please ask for a Green Apple Jolly Rancher.\n") 
elif dice_roll == 3:
    print("Squeal with glee, you got a three!\n")
    print("Please ask for a Cherry Jolly Rancher.\n") 
elif dice_roll == 4:
    print("Jump off the floor, the die says four!  \n")
    print("Please ask for a Grape Jolly Rancher.\n") 
elif dice_roll == 5:
    print("You rolled a five, that's no jive!\n")
    print("Please ask for a Water Melon Jolly Rancher.\n")
elif dice_roll == 6:
    print("You rolled a six, please take your pick!  Please ask for any flavor Jolly Rancher you like.\n")
else:
    x = 5
    while x != 0:
        print("Error.  Does not compute!  You did not enter a number from 1-6.  My memory will dump in ",x,"seconds.  Please restart me.\n")
        time.sleep(1)
        x += -1
    exit()
    
 

time.sleep(wait_time) # Pause.

# The next if / else statement will use inequalities for the check.
dice_roll_2d6 = int(input("Please roll the die twice and add the two numbers together in your head.  Type the number you rolled and press enter.\n"))

if dice_roll_2d6 == 2:
    print("Snake eyes wins no prize!\n")
    print("You get nothing!  Absolutely nothing!\n") 
elif dice_roll_2d6 <= 4:
    print("Don't play footsie, get yourself a Tootsie!\n")
    print("Please ask for a Tootsie Roll.\n") 
elif dice_roll_2d6 <= 10 :
    print("I canot spel, get yorself a caramel!\n")
    print("Please ask for a Caramel Creme.\n") 
elif dice_roll_2d6 == 11:
    print("I've got the seven, you just rolled an eleven!\n")
    print("Please ask for a Caramel Creme OR a Tootsie Roll.\n")
elif dice_roll_2d6 == 12:
    print("The sixes you rolled were double, now your teeth are in trouble.\n")
    print("Please ask for a Caramel Creme AND a Tootsie Roll.\n")
else:
    x = 5
    while x != 0:
        print("Error.  Does not compute!  You did not enter a number from 2-12.  My peripherals will fry in ",x,"seconds.  Please restart me.\n")
        time.sleep(1)
        x += -1
    exit()

    



