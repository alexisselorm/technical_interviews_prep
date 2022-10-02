
list1 = [12,20,23,45,55,23,66,99,1,2]
even=0
odd=0
for i in list1:
    if i %2==0:
        even+=1
    else:
        odd+=1
print(f"even is {even}")
print(f"odd is {odd}")
print(abs(odd-even))