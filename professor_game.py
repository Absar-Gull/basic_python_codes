import random

def get_level():
    while True:
        try:
            level=int(input("Insert the level(1/2/3): "))
            if (level == 1) or (level == 2) or (level == 3):
                return level
            else:
                continue
            
        except ValueError:
            continue
        except EOFError :
            break

def generate_sums_for_level_(level):
    while True:
        try:
            score=0
            startpoint=0
            endpoint=0
            if level==1:
                startpoint=0
                endpoint=9
            elif level==2:
                startpoint=10
                endpoint=99
            elif level==3:
                startpoint=100
                endpoint=999
            for i in range(0,10):
                x=random.randint(startpoint,endpoint)
                y=random.randint(startpoint,endpoint)
                z=x++y

                t=int(input(f"{x} + {y} : "))
                if z==t:
                    score+=1
                    continue
                else:
                    print("Try again")
                    for _ in range(0,2):
                      k=int(input(f"{x} + {y} : "))
                      if k!=z:
                        print("Try again")
                        print("1 Attemp left")
                        continue
                      else:
                        score+=1
                        break
            print("Your score is:", score)
            break
        except EOFError:
            break

                
def main():
    while True:
        try:
            n=get_level()
            generate_sums_for_level_(n)
            play_again=input("Do you want to play again? (y/n)")
            if play_again=="y":
                continue
            else:
                print("End of the Game")
                break
        
        except EOFError:
            print("End of the Game")
            break

print("Welcome to the calculater game.")
main()
