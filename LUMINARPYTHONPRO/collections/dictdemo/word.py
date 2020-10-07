line="hai hello hai hello"
words=line.split(" ")
print(words)
dict={}
for i in words:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
