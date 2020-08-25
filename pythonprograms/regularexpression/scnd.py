import re
pattern='[a-z]'
pat=re.finditer(pattern,"aba 4df")
for matc in pat:
    print(matc.start())
    print(matc.group())