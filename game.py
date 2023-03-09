import random 


def main():
    print("GUESS THE NUMBER")
    inp=(input("Enter the range of numbers you want to play in separated by ',': "))
    x=int((inp.split(','))[0])
    y=int((inp.split(','))[1])
    if x>y:
        print("Invalid range")
    n=0
    if y-x<50:
        n==3
    if y-x>100:
        n==30
    numb=random.randint(x,y)
    
    i=0
    while  i<=5:
        guess=int(input("Your guess: "))
        i+=1
        if guess>(numb+n):
                print("You should go down ")
        elif guess<(numb-n):
                 print ("You should go up")
        elif (numb-n)<=guess<=(numb+n) and guess!=numb:
                print("you are really close")        
        else:
            guess==numb
            print ("You have guessed right.Congratulations")
            break 
        print("number of guess left:", 6-i)
    print("The number is: ",numb)
if __name__=='__main__':
    main()