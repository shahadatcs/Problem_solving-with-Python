def Add(num):
    sum = 0
    while(num>0):
        temp = num%10
        sum = sum + temp 
        num = num // 10
    print(sum)
num = int(input())
Add(num)