f=open("wordd","r")
dict={}
for lines in f:
    word=lines.split(" ")
    print(word)
for wor in word:
    if wor   not in dict:
        dict[wor]=1
    else:
        dict[wor]+=1
for k,v in dict.items():
    print(k,",",v)