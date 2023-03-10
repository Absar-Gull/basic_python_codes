
def main():
    text=input("Enter the desired plate number: ")
    plate=text.lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    for char in s:
        if punc(char):
            return False 
    if not(96<ord(s[0])<123 and 96<ord(s[1])<123):
        return False
    if letters_after_numbers(s):
        return False
    else:
        return True


def letters_after_numbers(text):
    for i,char in enumerate(text):
        if char.isnumeric():
            letter_part=text[:i]
            numeric_part=text[i:]
            break
    if any_character_is_alphabet(numeric_part):
        return True
    if int(numeric_part[0])==0:
        return True
    
    else: 
        return False


def any_character_is_alphabet(s):
    for char in (s):
        if 96<ord(char)<123:
            return True
    else:
        return False

    

def punc(p):
    if p== "!" or p=="." or p=="," or p=="?":
        return True
    
    return False

main()
    

    
