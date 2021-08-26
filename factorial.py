import math
def factorial(n):

    for i in range(n):
        f = int(math.factorial(i))
        if f == n:
            i = 1
            break
        else:
            i = 0
    if i==1:
        print("yes")
    else:
        print("No")



number = int(input("please enter your number: "))

factorial(number)
