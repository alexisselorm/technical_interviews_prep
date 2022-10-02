sentences = []
print("How many sentences")
n = int(input())
print("What is your word")
word = input().lower()
for i in range(1,n+1):
    print("Enter sentence " + str(i))
    sentence = input().lower()
    sentences.append(sentence)

print("")
print("")
print("")
for sentence in sentences:
    if word in sentence:
        print(sentence)

for sentence in sentence:
    if word not in sentence:
        print(sentence)
        