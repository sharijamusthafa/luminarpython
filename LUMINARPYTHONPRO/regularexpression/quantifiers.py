import re
pattern="a{2}"
pat=re.finditer(pattern,"aabbabaaabba")
count=0
for matc in pat:
    print(matc.start())
    print(matc.group())

    count+=1
print(count)