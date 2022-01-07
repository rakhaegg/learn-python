class A :
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")
        super().method()

class C(B):
    def third_method(self):
        print("C method")


c = C()

c.another_method()
c.third_method()


