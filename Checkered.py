n = int(input("plase enter n: "))
m = int(input("enter m: "))
   
for i in range(n):
    for j in range(m):
        if (i+j) %2==0:
            print('*', end=" ")
        else:
            print('#', end=" ")
    print()
        
