# Using summation of first N natural numbers

def MissingNumber(n, arr):
    total =int((n+1)*(n+2)/2)
    sum_of_arr = sum(arr)
    return total - sum_of_arr

arr=[]
lenght = int(input('Enter a number: '))
for i in range(0, lenght):
    arr.append(int(input())) # input sequence nuber 1,2,....n
print(arr)

size =len(arr)
miss = MissingNumber(size, arr)
print(miss)
