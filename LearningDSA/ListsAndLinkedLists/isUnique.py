list1 = [1, 2, 3, 8,4,2,5,2,4, 5, 6]
emptyList = []


def isUnique(array1, array2):
    for i in range(len(array1)):
        if array1[i] not in array2:
            array2.append(array1[i])
        
        else:
            continue
    return array2

print(isUnique(list1,emptyList))