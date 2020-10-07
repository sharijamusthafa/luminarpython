import re
pattern='[abc]'
pat=re.finditer(pattern,"aba 4df")
for mat in pat:
    print(mat.start())
    print(mat.group())