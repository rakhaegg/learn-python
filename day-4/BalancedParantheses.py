class Stack :
    def __init__(self) :
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self , item):
        self.items.insert(0 , item)
    def pop(self):
        return self.items.pop(0)
    def print_stack(self):
        print(self.items)

s = Stack()

value = input()

for i in value:

    if i == '(':
        s.push('(')
    elif i  == ')':
        if s.is_empty() :
            s.push(')')
        else : 
            s.pop()
        

print("True" if s.is_empty() else "False")
