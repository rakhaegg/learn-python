
value1 , value2 = input() , input()


count = 0

for i in value1:
    
    if i == value2:
        count = count +1

print(int(count / len(value1) * 100))