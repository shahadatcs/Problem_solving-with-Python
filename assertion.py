'''
Assertions in any programming language are the debugging tools that help in the smooth flow of code. Assertions are mainly assumptions that a programmer knows or always wants to be true and hence puts them in code so that failure of these doesn’t allow the code to execute further. 

In simpler terms, we can say that assertion is the boolean expression that checks if the statement is True or False. If the statement is true then it does nothing and continues the execution, but if the statement is False then it stops the execution of the program and throws an error.


'''
# Python 3 code to demonstrate
# working of assert
 
# initializing number
# Example 1

#a = 4
#b = 0
 
# using assert to check for 0
#print('the value of a/b : ')
#assert b!=0, 'Zero Division Error'
#print(a/b)


# Example 2

batch =[40,50,60,30,20]
cut = 26
for i in batch:
    assert i>=26, 'Batch is rejected'
    print(str(i) + ' is ok')