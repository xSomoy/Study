import random
import time
iteration = 0
value = int(input("Provide Intial Value For The Stock: "))
highest_val = value
lowest_val = value

while True:
    index = random.randrange(0, 2)
    prev_val = value
    if index == 0:
        value = value - 1
    else:
        value = value + 1
    iteration += 1
    if value > highest_val:
        highest_val = value
    if lowest_val > value:
        lowest_val = value

    print(f'\nIteration:{iteration} ')
    print(f'High: ${highest_val} Low: ${lowest_val}')
    print(f'Current Stock Value: ${value}')
    time.sleep(1)
