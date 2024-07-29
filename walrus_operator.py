happy=True
print(happy)
print(happy := False)
#without walrus operator
foods=[]
while True:
    food=input("what food do you like")
    if food=="quit":
        break
    foods.append(food)

#by walrus operator
foods=[]
while(food:=input("whats your fav food")!="quit"):
    foods.append(food)
