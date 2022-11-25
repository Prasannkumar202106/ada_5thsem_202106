#write a program to check Primality Test using Fermat method #
import random
def fermat(n):#start the fermat function
    A = random.randint(1, n-1) #  A can have random number from 1 to p-1
    if(pow(A, n-1)%n != 1):
        return False
    return True  #else condition
x= int(input("enter the number  for check wheather it is prime or not \n") )
z=fermat(x)      
if z == True:
    print("{} is a prime ".format(x))
elif z==False:
    print("{} is not prime".format(x))
