#----------------------------------
#
# IPND Stage 2 Final Project
#
#----------------------------------
# Norbert's Fill-in-the-Blanks Mercedes quiz
#
# Developer: Norbert Neuber


"""
Project Submission

In this stage, you will use the Python programming language 
to build your own quiz. You will use a fill-in-the blank 
style to create a quiz that can even be used as a study tool 
to help you remember important vocabulary.

1 - Game Review
In this portion of the review, your reviewer will be checking 
to make sure the game works the way it's supposed to. See the 
rubric below for exact specs.

2 - Code Review
Your reviewer will also look at the Python code you've written 
and provide feedback on:

Use of Variables: Your code should take advantage of variables 
and variable names should reflect the values they store.
Functions: Your code should use functions appropriately to 
avoid repetition. Function parameters should have logical names 
and should all be used in the body of the function.
Appropriate use of Data: Data types (strings vs lists for example) 
should be used appropriately.
Appropriate use of other coding techniques: Your code should use 
statements like if, elif, else, while, etc... appropriately.
Each function includes a comment: Comments explain function 
behavior, inputs, and outputs (if applicable.)
"""

"""
Game Basics Game has 3 or more levels and each level contains 
4 or more blanks to fill in
"""
level_index_list = [easy, medium, hard]

easy_quiz = "Mercedes-Benz is a global ___1___ manufacturer and a division of the German company ___2___ AG. The brand is known for luxury vehicles, buses, coaches, and trucks. The headquarters of __3__-Benz are in __4__, Baden-Württemberg, Germany."
easy_answer = ["automobile", "Daimler", "Mercedes", "Stuttgart"]

medium_quiz = "The first car. In __1__, Carl Benz is awarded German patent number 37435 for a __2__-wheeled, self-propelled "Motorwagen". With a rear-mounted __3__-cylinder engine, the first __4__ forever changes the way people move, and sparks a legacy of innovation that continues to this day"
medium_answer = ["1886", "three", "single", "automobile"]

hard_quiz = "The first female driver: __1__ Benz, Carl's __2__, decided to help promote his invention by taking it on a 120-mile tour __3__ his prior knowledge. She also served as her own __4__ on the trip."
hard_answer = ["Bertha","wife","without","mechanic"]


"""
Beginning the Game
Immediately after running the program, user is prompted 
to select a difficulty level from easy / medium / hard
"""

user_input = raw_input("Enter a difficulty level easy / medium / hard. What is your choise? ").lower()

for user_input in level_index_list:
	print "You have choosen %s as your difficulty level" % (user_input)
    return user_input

"""
Once a level is selected, game displays a fill-in-the-blank 
and a prompt to fill in the first blank.
"""



"""
When player guesses correctly, new prompt shows with correct 
answer in the previous blank and a new prompt for the next blank
When player guesses incorrectly, they are prompted to try again
"""
