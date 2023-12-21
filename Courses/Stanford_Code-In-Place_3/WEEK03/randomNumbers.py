# this is necessary if you want to use random numbers
import random

def main():
    for i in range(10):
        value = random.randint(1, 100)
        print(value)

if __name__ == '__main__':
    main()