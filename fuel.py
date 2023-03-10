
while True:
    text=input("enter the ratio (p/q):")
    entities=text.split(sep='/')
    
    try:
        x=int(entities[0])
        y=int(entities[1])

        z=(x/y)*100
        while z>100:
            print ("Not a valid ratio")
            text_update=input("Enter the ratio:")
            text=text_update
        if 100>=z>=99:
            print("F")
        elif z<=1:
            print("E")
        else:
            print(round(z),"%")
        break
        
    except ValueError :
        print("Not a valid ratio.")
    except ZeroDivisionError:
        print("Not a valid ratio.")

