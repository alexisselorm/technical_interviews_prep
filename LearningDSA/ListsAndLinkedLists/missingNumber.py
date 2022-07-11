from re import I


def missingNumber(myList, totalCount):
    expectedSum = totalCount*((totalCount+1)/2)
    actualSum = 0
    for i in myList:
        if i in myList:
            actualSum += i
        return int(expectedSum - actualSum)
