# string vs. float vs. int Python Data Types -- 02/11/20, 11:38AM, Ryan Kelley
import time

# Inputting the three variable types. 
my_string = str(input("Please type a sentence and then press enter."))
print("This type of variable is a STRING.") 
print(my_string)
my_float = float(input("Please type a decimal number and then press enter."))
print("This type of variable is a FLOAT.")
print(my_float)
my_int = int(input("Please type an integer and then press enter."))
print("This type of variable is an INTEGER.") 
print(my_int)
print("Next I will perform some functions with those different variables.")
time.sleep(3)

print("First I will combine the two strings.  This is known as CONCATENATION.")
print(my_string + my_string)
time.sleep(2)
print("Next I will add the integers together.")
print(my_int + my_int)
time.sleep(2)
print("Next I will add the two floats together.") 
print(my_float + my_float) 

print(my_int + my_float)
print(my_int + my_string)

float = 3.14
my_string1 = "3.14"


