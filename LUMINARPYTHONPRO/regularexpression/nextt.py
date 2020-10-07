import re
pattern='[^a-zA-Z0-9]'
pat=re.finditer(pattern,"aba  #$4df")
for matc in pat:
    print(matc.start())
    print(matc.group())