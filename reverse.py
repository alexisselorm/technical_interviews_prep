# # n = int(input())
# # element = input()


# # list1 = element.split(" ")


# # list1.reverse()
# # print(list1)

# list1 = [1, 2, 3, 4, 5, 6, 7]


# # print("1 2 3 4".split(" "))
# list1 = list1[::-1]
# print(*list1)

# # for elm in list1:
# #     print(elm,end=" ")
# # print(" ".join(list1))

n = 2  # how many numbers to accept
numbers = [int(num) for num in input().split(" ", n-1)]

print(numbers)