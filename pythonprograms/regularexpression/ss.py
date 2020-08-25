import re
pattern="\w"
pat=re.finditer(pattern,"aba  #$4df")
for matc in pat:
    print(matc.start())
    print(matc.group())