x = [6, 4, 2, 9]
x = x[::-1]
print(x[0]+x[2])


print("{0}{1}{0}".format("abra", "cad"))



def func(x):
  res = 0
  for i in range(x):
      
     res += i
     print(res)
  return res

print(func(4))


N = int(input())
#your code goes here


result = 0
for i in range(0 , N+1) : 

    result += i


print(result)


text = input()
word = input()

def search(text , word) : 

    if text.count(word) == 0:
        return "Word not found"
    else :  
        return "Word found"

print(search(text, word))




