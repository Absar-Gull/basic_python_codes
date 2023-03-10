a = input("Expression: ") 
x, y, z = a.split(" ")

if y=="+":
    print(int(x) + int(z))
elif y=="*":
    print(int(x) * int(z))
elif y=="-":
    print(int(x) - int(z))
elif y=="/":
    print(int(x) / int(z))
else:
    print(invalid)