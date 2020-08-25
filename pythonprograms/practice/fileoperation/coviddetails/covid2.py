f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    deathcount=data[7]
   # print(state,",",deathcount)
    if state not in dict:
        dict[state]=deathcount
    else:
        dict[state]=deathcount
for k,v in dict.items():
    print(k,",",v)