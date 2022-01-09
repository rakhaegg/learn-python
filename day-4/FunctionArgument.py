


def my_func(x , y=7 , *args , **kwargs):
    print(kwargs)



my_func(2, 3 ,4 ,5, 6, a=7 ,b = 8)


def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)


for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)