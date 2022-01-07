primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[4])
print(primes[primes[4]])



pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    None: "True",
    "apple" : 1
}


print(pairs.get(str(1)))
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))



fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4 , 0))
print(fib.get(7 , 5))

print(fib.get(4, 0) + fib.get(7, 5))
