import re
pattern="\D"
pat=re.finditer(pattern,"aba  #$4df")
for matc in pat:
    print(matc.start())
    print(matc.group())