from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

# turn180 function turns karel 180 degree
def turn180():
    turn_left()
    turn_left()

# turn_right function uses a for loop
# rather than using "turn_left()" command 3 times
def turn_right():
    for i in range(3):
        turn_left()
        
# Using a while loop and the "front_is_clear()" condition
# we can move karel as far as the front is clear
def front_clear():
    while front_is_clear():
        move()
    
def main():
    while no_beepers_present():
        move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
# using the facing_north() codition to rotate our karel 180 degree 
    if facing_north():
        turn180()
    front_clear()
    turn_right()
    front_clear()
    turn180()
        
   

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()