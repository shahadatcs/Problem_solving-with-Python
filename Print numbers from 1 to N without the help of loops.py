def calculate(initial, last):
    if(initial <= last):
        print(initial, end=' ')
        calculate(1+initial, last)


N = int(input())
calculate(1,N)

