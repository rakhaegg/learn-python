

class SpecialString :
    def __init__(self , cont) :
        self.cont = cont
    
    def __truediv__(self , other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont , line , other.cont])

spam = SpecialString("spma")
hello = SpecialString("Hello World")
print(spam / hello)




class SpecialString:
    def __init__(self , cont):
        self.cont = cont
    def __gt__(self , other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


import random 
class VagueList:
    def __init__(self , cont):
        self.cont = cont
    def __getitem__(self , index):
        return self.cont[index + random.randint(-1 , 1)]
    def __len__(self):
        return random.randint(0 , len(self.cont)*2)
    
vague_list = VagueList(["A" , "B" , "C" , "D" , "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])