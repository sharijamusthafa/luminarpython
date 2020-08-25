pattern="ABABACAA"
dict={}
print(pattern)
for char in pattern:
   # print(char,end=" ")
    if char not in dict:
        dict[char]=1
    else:
        dict[char]+=1
for k,v in dict.items():
    print(k,",",v)