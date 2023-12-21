from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
# turn_right function uses a for loop
# rather than using "turn_left()" command 3 times
def turn_right():
    for i in range(3):
        turn_left()

def nextCol():
    for i in range(4):
        move()
        
def beepPutter():
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move()
        

def main():
    turn_left()
    beepPutter()
    turn_right()
    nextCol()
    turn_right()
    beepPutter()
    turn_left()
    nextCol()
    turn_left()
    beepPutter()
    turn_right()
    nextCol()
    turn_right()
    beepPutter()
    turn_left()
    
    
    
    
if __name__ == '__main__':
    main()