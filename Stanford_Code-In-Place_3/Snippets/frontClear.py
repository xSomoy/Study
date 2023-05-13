# Using a while loop and the "front_is_clear()" condition
# we can move karel as far as the front is clear
def front_clear():
    while front_is_clear():
        move()
    