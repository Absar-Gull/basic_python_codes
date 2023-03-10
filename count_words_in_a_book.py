import os
from pprint import pprint
import re


words=[]
no_of_words=0
with open("codetotext.txt", "r") as f:
    book=f.read()
book=book.lower().strip()
book=re.split(r"\W+",book)
print(book)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|"'''

uninteresting_words = [
    "the", "a", "to", "if", "is", "in" "it", "of", "and", "or","on", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"
    ]


k=len(book)-1
print(k)
for i in range(k):
    if book[i] not in punctuations and book[i] not in uninteresting_words :
        no_of_words+=1
print(no_of_words)   




























uninteresting_words = [
    "the", "a", "to", "if", "is", "in" "it", "of", "and", "or","on", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"
    ]


