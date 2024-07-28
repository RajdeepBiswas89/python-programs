class parentclass:
    def parent_method(self):
        print("this is a parent method")
class child_class(parentclass):
    def child_method(self):
        print("this is child method")
    def parent_method(self): #calling the parent method of the child class
        print("this is a parent method of the child class")
        super().parent_method() #calling the parent method of the parent class
obj1=child_class()
obj1.child_method()
obj1.parent_method()