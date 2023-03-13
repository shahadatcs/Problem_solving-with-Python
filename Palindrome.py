# Palindrome string
def palindhome_str(str):
    if str == str[: : -1]:
        print('Valid Palindrome String: ', str)
    else:
        print('InValid Palindrome String: ', str)

string = str(input())
palindhome_str(string)

# Palindrome Number
def palindhome_num(num):
    n = num 
    rev = 0
    while(num>0):
        div = num % 10
        rev = rev*10 + div
        num = num//10
    if(n==rev):
        print('It is valid Palindrome Number: ', rev)
    else:
        print('It is Invalid Palindrome Number: ', rev)
num = int(input())
palindhome_num(num)


