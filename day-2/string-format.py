

print("{0}{1}{0}".format("abra" , "cad"))


a = "{x} , {y}".format(x = 5 , y = 12)
print(a)



result = ", ".join(["spam", "eggs", "ham"])
print(result)

result = "rakha ,  elang ,  gunawn".split(", ")
print(result)


print(abs(42))

nums = [55 , 44 , 33 , 22 , 11]


if all([i < 5 for i in nums]):
    print("All larger than 5")


if any([i % 2 == 0 for i in nums]):
    print("At least one is even")


for v in enumerate(nums):
    print(v)