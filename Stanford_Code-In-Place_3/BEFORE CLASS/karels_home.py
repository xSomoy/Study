from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_back()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    
    # add your code here
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_back():
    turn_left()
    turn_left()

    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()