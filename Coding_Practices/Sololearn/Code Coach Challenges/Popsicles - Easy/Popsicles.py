#Popsicles Solution

siblings = int(input())
popsicles = int(input())

#your code goes here
de = popsicles % siblings 
if(de == 0):
    print('give away')
else: print ('eat them yourself')