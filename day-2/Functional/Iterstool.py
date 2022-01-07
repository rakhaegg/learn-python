from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break

from itertools import accumulate , takewhile
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x : x<=6 , nums)))


from itertools import takewhile
nums = [2 , 4 , 6 , 7 , 9 , 8]
a = takewhile(lambda x :  x %2 == 0 , nums)

print(list(a))


from itertools import product , permutations

letter = ("A" , "B")

print(list(product(letter , range(2) )))
print(list(permutations(letter)))



from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))


