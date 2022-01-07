nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums

print(nums)





nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums


def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))