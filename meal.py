def main():
    x=input("What is the time?")
    t=convert(x)
    if 7<=  t <=8:
        print("Its time for breakfast")
    elif t >=12 and t<=13:
        print("Its time for lunch")
    elif t>=18 and t<=19:
        print("Its time for dinner")
def convert(time):
    hr,min= time.split(':')
    n=(int(min)/60)
    return (int(hr)+int(n))

main()