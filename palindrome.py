 

number = ((input("enter number")))
l=len(number)
number = int(number)
numb_list=[]
palindrome = 0
for i in range(1,l+1):
    digit = (number%10**i)//(10**(i-1))

    palindrome = digit*10**(l-i) + palindrome
    
if number == palindrome:
    print('palindrome')
else:
    print('not palindrome')

    


   

