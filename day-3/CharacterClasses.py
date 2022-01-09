import re

pattern = r"[aeiou]"

if re.search(pattern , "grey"):
    print("Match 1")

if re.search(pattern , "qwertyuiop"):
    print("Match 2")

if re.search(pattern , "rhythm myths"):
    print("Match 3")



import re

pattern = r"[A-Z][A-z][0-9]"

if re.search(pattern , "LS8"):
    print("Match 1")

if re.match(pattern , "E3"):
    print("Match 2")

if re.match(pattern , "lab"):
    print("Match 3")


import re

pattern = r"[^A-Z]"

if re.search(pattern , "this is all quiet"):
    print("Match 1")

if re.search(pattern , "AbCdEfG123"):
    print("Match 2")

if re.search(pattern , "THISISALLSHOUTING"):
    print("Match 3")



import re 
pattern = r"egg(spam)*"

if re.match(pattern , "egg"):
    print("Match 1")

if re.match(pattern , "eggspamspamegg"):
    print("Match 2")

if re.match(pattern , "spam"):
    print("Match 3")





import re

pattern =   r"g+"

if re.match(pattern , "g"):
    print("Match 1")

if re.match(pattern , "gggggggggggggggggggg"):
    print("Match 2")

if re.match(pattern , "abc"):
    print("Match 3")


import re 

pattern = r"ice(-)?cream"


if re.match(pattern , "ice-cream"):
    print("Match 1")

if re.match(pattern , "icecream"):
    print("Match 2")

if re.match(pattern , "sausages"):
    print("Match 3")



import re

pattern = r"9{1,3}$"

if re.match(pattern , "9"):
    print("Match 1")

if re.match(pattern , "999"):
    print("Match 2")

if re.match(pattern , "999"):
    print("Match 3")