def bubble_sort(lis):
    for i in range(0, len(lis)-1):
        for j in range(len(lis)-1):
            if(lis[j]> lis[j+1]):
                lis[j],lis[j+1] = lis[j+1], lis[j]
    return lis
lis = [ 5,3,8,6,7,2]
print('The sorted list is: ', bubble_sort(lis))