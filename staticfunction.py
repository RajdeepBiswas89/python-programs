class maths:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):#no need of passing self as an argument while using static method
        return a+b
a=maths(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(5,5))#way of calling static method (class_name.function_name)