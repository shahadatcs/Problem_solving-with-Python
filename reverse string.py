# with for loop and function Declaration
def reverse_string(str):
    str1 = ''
    for i in str:
        str1 = i+str1
    return str1
st=str(input())
print(reverse_string(st))

end='/n'

#with while loop
def while_reverse(str):
    st1=str
    str1 = ''
    st = len(st1)
    while st> 0:
        str1 = str1 + st1[st-1]
        st = st-1
    return str1

string = str(input())
print(while_reverse(string))

end='/n'

# Using Slice operator

def slice_reverse(str):
    str = str[: : -1]
    return str

string = str(input())
print(slice_reverse(string))

# with reverse function and join

def reverse_function(str):
    return ''.join(reversed(str))

string = str(input())
print(reverse_function(string))

# reverse string with recursion
def recursion_fun(str):
    #str = len(str)
    if len(str) == 0: # Checking the lenght of string  
        return str 
    else: 
        return recursion_fun(str[1:]) +str[0]
string = str(input())
print(recursion_fun(string))