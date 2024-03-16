# Name: Daniel Rein M. Cosare
# Course/Section/Year: BSCPE 1-2
# Activity/Program #2: Write a program that will ask you to input your name and your dream job. Print them in a fancy way.

# import module
import pyfiglet


# This code inputs the user's info
name = str(input('\033[36m' + "Please enter your name: "))
dream_job = str(input('\033[33m' + "Please enter your dream job: "))

# Concatenate the strings together
message = ("Your name is " + name +
           " and your dream job is " + dream_job)

# Use pyfiglet to create fancy art
result = pyfiglet.figlet_format(message, font="digital")
print('\033[32m' + result)
