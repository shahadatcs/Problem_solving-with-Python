'''# check prime or not
num = int(input())
if num > 1:
    for i in range(2, (num/2)+1):
        if (num%i) == 0:
            print(num, 'is not a prime number')
            break
        else:
            print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')
    
# print prime number in a range

low = int(input())
high = int(input())

for num in range (low, high + 1):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print(" %d" %num, end = '  ')

'''

# print prime number in range

p = int(input())

for i in range(2, p+1):
    c = 0
    for j in range(2, i//2+1):
        if(i%j==0):
            c+=1
    if(c<=0):
        print(i, end=' ')
