def fizzBuzz(n):
    # Write your code here
    i = 1
    while (i <= n):
        if(i % 5 == 0 ) and (i % 3 == 0):
            print("FizzBuzz")
        elif ( i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
        i=i+1
        

fizzBuzz(n)