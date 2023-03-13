
lt = []
# asking number of elements to put in list
n = int(input('Enter a number of elements list: '))

# iterating till num to append elements in list
for i in range(0, n):
    element = int(input('Enter list Element: '))
    lt.append(element)
print('Max number of list: ', max(lt))

lis = []
m = int(input())
for i in range(0, m):
    lis.append(int(input()))
lis.sort()
print(lis[-1])

#lst = [20, 10, 20, 4, 100]
#print(max(lambda x : int(x), lst))

from functools import reduce
lst = [20, 10, 20, 4, 100]
largest_elem = reduce(max, lst)
print(largest_elem)


#Function to find the largest element in the list
def FindLargest(itr,ele,list1):
  if itr == len(list1): #Base condition
    print("Largest element in the list is: ", ele)
    return
  if ele < list1[itr]: #check max condition
    ele = list1[itr]
  FindLargest(itr+1,ele,list1) #recursive solution
  return
list1=[2,1,7,9,5,4]
FindLargest(0,list1[0],list1)