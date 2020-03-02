import re
s = input()
pattern = re.compile(s, re.IGNORECASE)
try:
    while True:
        temp = input().replace(" ","")
        temp = pattern.sub("",temp)
        print(temp)
except EOFError:
    pass


'''
pattern = re.compile("hello", re.IGNORECASE)
pattern.sub("bye","hello HeLLo HELLO")
'''