import re
password= input()
flag = 0
while True:
    if (len(password)<= 8):
        flag = -1
        break
    elif not re.search('[a-z]', password):
        flag = -1
        break
    elif not re.search('[A-Z]', password):
        flag = -1
        break
    elif not re.search('[0-9]', password):
        flag = -1
        break
    elif not re.search('[_@$]', password):
        flag = -1
        break
    elif not re.search('\s', password):
        flag = -1
        break
    else:
        flag = 0
        print('Valid password')
        break
if flag == 1:
    print('Not Valid password') 

# Second way to check password
l, u, p, d = 0, 0, 0, 0
s = input()

if (len(s)> 8):
    for i in s:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            p+=1
        if (i=='@' or i=='$' or i=='_'):
            d+=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+u+p+d==len(s)):
    print('Valid password')
else:
    print('InValid password')
    
        