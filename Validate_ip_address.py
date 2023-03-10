import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))
    if validate:
        print("Valid")
    else:
        print("Invalid")


def validate(ip):
    valid = re.match(r"^25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?\.^25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?\.^25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?\.^25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?$",ip)
    if valid:
        return True
    else:
        return False




if __name__ == "__main__":
    main()



