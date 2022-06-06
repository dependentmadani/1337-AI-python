import sys

n = len(sys.argv)
phrase_initial = ""
for i in range(1,  n):
    phrase_initial += " " +sys.argv[i]

phrase_final = ""
for i in phrase_initial:
    if (i.isupper()):
        phrase_final += i.lower()
    elif (i.islower()):
        phrase_final += i.upper()
    else:
        phrase_final += i

print(phrase_final[::-1])