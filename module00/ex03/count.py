# import sys
#!/usr/bin/python
import string

def text_analyzer(str, __doc__):
    if (not str):
        print("What is the text to analyze?")
        str = input()
    print("The text contains ", len(str) , " character(s):")
    sum = 0
    for i in str:
        if (i.isupper()):
            sum += 1
    print("- ",  sum , " upper letter(s)")
    sum = 0
    for i in str:
        if (i.islower()):
            sum += 1
    print("- ",  sum , " lower letter(s)")
    sum = 0
    for i in str:
        if i in string.punctuation:
            sum += 1
    print("- ",  sum , " punctuation mark(s)")
    sum = str.count(" ")
    print("- ",  sum , " space(s)")
    return


# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")

# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")