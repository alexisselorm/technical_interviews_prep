from more_itertools import first


array1=[84,85,86,87,85,99,90,83,23,45,1,2]

def firstSecond(array):
    a= array
    a.sort(reverse=True)
    print(a)
    second = 0
    first = a[0]
    second = 0
    second = a[1:2][0]
    return first,second
    # print(second)
    # for element in array:
    #     if element != first:
    #         second = element
    #         return first,second
    
print(firstSecond(array1))