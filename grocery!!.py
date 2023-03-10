grocery={}
grocery_final={}
i=0
while True :
    text=input("Grocery item: ")
    if text=="d":
        break
    i+=1
    grocery[i]=text
    
    
cart=list(grocery.values())
print(cart)
for _ in cart:
    n=cart.count(_)
    print(n)

grocery
print(grocery)