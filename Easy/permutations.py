n = 4
list1 = []
list2 = []
for i in range(n):
    element = int(input())
    list1.append(element)
for j in range(n):
    element = int(input())
    list2.append(element)

list1 = set(list1)
list2 = set(list2)


def ispermutation(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        if len(l1.difference(l2)) == 0:
            return "YES"
        else:
            return "NO"


print(ispermutation(list1, list2))
