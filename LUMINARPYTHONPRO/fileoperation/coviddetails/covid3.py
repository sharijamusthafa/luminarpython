f=open("covid_19_india.csv","r")
dict={}
dictt={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    deathcount=data[7]
    confirmedind=data[8]
   # print(state,",",deathcount)
    if state not in dict:
        dict[state]=deathcount
        dictt[state]=confirmedind
    else:
        dict[state]=deathcount
        dictt[state]=confirmedind
for k,v in dict.items():
    print(k,",",v)
for l,m in dictt.items():
    print(l,",",m)