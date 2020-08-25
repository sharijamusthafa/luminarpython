from re import *
pattern='[A-Z]'
pat=finditer(pattern,"abaAC 4dfZ")
for matc in pat:
    print(matc.start())
    print(matc.group())