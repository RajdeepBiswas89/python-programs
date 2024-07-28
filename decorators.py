def greet(fx):
    def modified_fx(*args,**kwargs):
        print("good morning user")
        fx(*args,**kwargs)
        print("thanks for using our website")
        return modified_fx()
@greet
def hello():
    print("....transcation in process....")
@greet
def addition(a,b):
    print(a+b)
addition(1,2)
hello()