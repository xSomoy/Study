from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
# Using a while loop and the "front_is_clear()" condition
# we can move karel as far as the front is clear
def one_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
# turn180 function turns karel 180 degree
def turn180():
    turn_left()
    turn_left()
    
# Using a while loop and the "front_is_clear()" condition
# we can move karel as far as the front is clear
def front_clear():
    while front_is_clear():
        move()

# turn_right function uses a for loop
# rather than using "turn_left()" command 3 times
def turn_right():
    for i in range(3):
        turn_left()

def main():
    while facing_east():
        if front_is_blocked():
            pass
        one_row()
        turn180()
        front_clear()
        turn_right()
        move()
        turn_right()
   
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()