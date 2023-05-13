from karel.stanfordkarel import *

# Here is a place to program your Section problem
def to_next_beeper():
    while no_beepers_present():
        move()
# turn_right function uses a for loop
# rather than using "turn_left()" command 3 times
def turn_right():
    for i in range(3):
        turn_left()
        
def pile_beepers():
    to_next_beeper()
    turn_left()
    for i in range(3):
        if front_is_clear():
            move()
            put_beeper()
            move()
            put_beeper()
            turn_right()
            move()
            turn_right()
            put_beeper()
            move()
            put_beeper()
            move()
            put_beeper()
    turn_left()


def main():
    while facing_east():
        pile_beepers()
 
    

if __name__ == '__main__':
    main()