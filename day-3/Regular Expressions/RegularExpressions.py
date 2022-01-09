import re

pattern = r"spam"



if re.match(pattern , "spamspamspam"):
    print("Match")
else : 
    print("No Match")



import re
pattern = r"spam"

if re.match(pattern , "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

if re.search(pattern , "eggspamsausagespam"):
    print("Match")
else :
    print("No Match")

print(re.findall(pattern , "eggspamsausagespam"))



import re
pattern = r"pam"

match = re.search(pattern , "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


import re
str = "My name is David. Hi David. "
pattern = r"David"
newstr = re.sub(pattern , "Amy" , str)
print(newstr)