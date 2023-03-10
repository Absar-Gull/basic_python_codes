import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url=re.search(r'https?://(www)?\.?youtube\.com/watch?(\w.+)',s)
    if url:
        return (f"http://youtu.be/{url.group(2)}")





if __name__ == "__main__":
    main()