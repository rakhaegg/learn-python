text = input()




count = 0

for i in text.split(" "):
    count = count + 1

count2 = len(text) - text.count(' ')
print(count2/count)
