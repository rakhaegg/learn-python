def decot(func) : 
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

#decor
@decot
def print_text():
    print("Hello World")

decorated = decot(print_text)
decorated()