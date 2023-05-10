from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
     # add your code here
    move()
    for i in range(10):
        pick_beeper()
    move()
    move()
    for i in range(10):
        pick_beeper()
    move()
    move()
    for i in range(10):
        pick_beeper()
    move()

   
    


    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()