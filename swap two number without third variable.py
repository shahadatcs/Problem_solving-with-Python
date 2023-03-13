x,y = int(input()), int(input()) 

# very simple
x,y = y,x 

print("Value of x : ", x, " and y : ", y)

# with Addition Subtraction thinking
x = x+y
y = x-y
x = x-y
print("Value of x : ", x, " and y : ", y)


# with bitwise operator

x^=y
y^=x
x^=y

print("Value of x : ", x, " and y : ", y)


