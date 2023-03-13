# check palindrome number
def palindrome(num):
    temp = num
    rev = 0
    while(num>0):
        div = num%10
        rev = rev*10 + div
        num = num//10
    if( temp == rev ):
        print('Valid Palindrome Number')
        sum = 0
        while( temp>0 ):
            div = temp%10
            sum = sum + div
            temp = temp//10
        print(sum)
            
    else:
        print('Invalid Palindrome Number')
        

    
num = int(input())
palindrome(num)