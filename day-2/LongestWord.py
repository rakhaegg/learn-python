txt = input()

splitString = txt.split(' ')

max = 0
word = ""
for i in splitString :
    if len(i) > max :
        word = i
        max = len(i)
    

print(word)