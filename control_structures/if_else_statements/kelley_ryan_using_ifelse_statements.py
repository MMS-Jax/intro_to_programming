# Using if / else Statements, Ryan Kelley, February 05, 2020.  Version 0.25


import random # This is a special library built-in to Python.  It has special methods, in this case .shuffle() that I will use in this code. 
import time # This lets us call the sleep() method which pauses the program for a specified number of seconds.

print("""
   __    __       _______. __  .__   __.   _______                                                                 
  |  |  |  |     /       ||  | |  \ |  |  /  _____|                                                                
  |  |  |  |    |   (----`|  | |   \|  | |  |  __                                                                  
  |  |  |  |     \   \    |  | |  . `  | |  | |_ |                                                                 
  |  `--'  | .----)   |   |  | |  |\   | |  |__| |                                                                 
   \______/  |_______/    |__| |__| \__|  \______|                                                                 
   __   _______         ___    _______  __           _______. _______                                              
  |  | |   ____|       /  /   |   ____||  |         /       ||   ____|                                             
  |  | |  |__         /  /    |  |__   |  |        |   (----`|  |__                                                
  |  | |   __|       /  /     |   __|  |  |         \   \    |   __|                                               
  |  | |  |         /  /      |  |____ |  `----..----)   |   |  |____                                              
  |__| |__|        /__/       |_______||_______||_______/    |_______|                                             
       _______..___________.    ___   .___________. _______ .___  ___.  _______ .__   __. .___________.    _______.
      /       ||           |   /   \  |           ||   ____||   \/   | |   ____||  \ |  | |           |   /       |
     |   (----``---|  |----`  /  ^  \ `---|  |----`|  |__   |  \  /  | |  |__   |   \|  | `---|  |----`  |   (----`
      \   \        |  |      /  /_\  \    |  |     |   __|  |  |\/|  | |   __|  |  . `  |     |  |        \   \    
  .----)   |       |  |     /  _____  \   |  |     |  |____ |  |  |  | |  |____ |  |\   |     |  |    .----)   |   
  |_______/        |__|    /__/     \__\  |__|     |_______||__|  |__| |_______||__| \__|     |__|    |_______/    
                                                                                                                   
                                       by Ryan Kelley, February 05, 2020 Version 0.25
""")
print("Hello $user, this program will help you learn how to use if / else statements in your code.  If you have any questions while using this program please raise your hand.\n")
user0 = str(input("$user, by what name should I call you?  Please, type your firt and last name and then press ENTER on your keyboard.\n")) # Create a variable named user and assign it a value.
# In Python, = is the English equivalent of "Make the thing on the left have the same value as the thing on the right."  

time.sleep(2) # Pause for two seconds. 

# The following lines of code create three slices of the user name and then rearranges them. 
user1 = user0[0:3]
user2 = user0[4:7]
user3 = user0[8:len(user0)]
user4 = user3 + user2 + user1

print("Your parents really named you",user4,"?\n")
name_correct = input("Is this really what I should call you?  [Type Yes or No, then press ENTER.]\n") # Create the variable name_correct and assign it a value. 
name_correct = name_correct[0] # This assigns the name_correct variable to JUST the first letter of the user's answer. 
name_correct = str.lower(name_correct) # This assigns the name_correct variable to the lower case version of that first letter.

time.sleep(2) # Pause for two seconds. 


# Our first if / else statement starts here.  It will check the VALUE of the name_correct variable and then test it against each CONDITION.

if name_correct == "y": # == is the English equivalent of "Is the thing on the left the same as the thing on the right?"
    # If they answer yes just leave user0 variable alone and continue on in the program.
    print("Ok, ",user0,"it is!\n")
elif name_correct == "n":
    # On the next line we will have the user re-type their name.  
    user0 = str(input("I am sorry.  I experienced a memory error in one of my circuits.  Please retype your name and press enter.\n"))
    print("Ahh! Yes,",user0,"that's more like it!\n")
else:
    print("Something has caught fire.  Emergency!  Prepare for crash.  Restart the program please.  Please enter Yes or No only.\n")

time.sleep(2) # Pause for two seconds.

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
    print("Error.  Does not compute!  You did not enter a number from 1-6.  Please restart the program.\n")
    exit()

time.sleep(3) # Pause for three seconds.

# The next if / else statement will use inequalities for the check.
dice_roll_2d6 = int(input("Please roll the die twice and add the two numbers together.  Type the number you rolled and press enter.\n"))

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
    print("Error.  Does not compute!  You did not enter a number from 2-12.  Please restart the program.\n")
    exit()

    
# We will work together to write one more if / else statement for practice.  
#if ____________: # Conditional Statement
    # Code to run.
#elif __________:
    # Code to run.
#else:
    # Code to run.


