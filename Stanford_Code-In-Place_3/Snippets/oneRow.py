# Using a while loop and the "front_is_clear()" condition
# we can move karel as far as the front is clear
def one_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()