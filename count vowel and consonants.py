string = input('Enter a string: ')
#string.lower() #call the lower function to avoid upper case letter
v, c = 0, 0
for i in string:
    if(i=='A' or  i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v+=1
    else:
        c+=1
print('The number of vowels: ', v)
print('The number of consonants: ', c)
