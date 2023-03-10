import random
import sys
from pyfiglet import Figlet

f=Figlet()
fts=f.getFonts()
random_font=random.choice(fts)

if len(sys.argv)==1:
    g=Figlet(font=random_font)
    text=input("Text: ")
    print(g.renderText(text))

elif len(sys.argv)==3:
    first_argument=sys.argv[1]
   
    if first_argument=="-f" or first_argument=="--font":
        ft=sys.argv[2]
       
        if ft in fts:
            f=Figlet(font=ft)
            text=input("Text: ")
            print(f.renderText(text))
        else:
            sys.exit("Input Error")
    
    else:
        sys.exit("Input Error")

else: 
    sys.exit("Input Error")