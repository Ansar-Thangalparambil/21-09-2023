class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
A(1)
A(2)
print(obj1+obj2)
obj3 = A("HELLO")
obj4 = A("WELCOME")
print(obj3+obj4)
