row = int(input('please enter number of row: '))
column = int(input('please enter number of column: '))

for i in range(1, row+1):
    for n in range(1, column+1):
        print(i*n, end=' ')
    print()
