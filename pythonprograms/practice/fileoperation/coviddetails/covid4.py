f=open("covid_19_india.csv","r")
dict={}
clist=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]

    confirmed=data[8]
   # print(state,",",deathcount)
    if state not in dict:
        dict[state]=confirmed

    else:
        dict[state]=confirmed
#sum=0
#for k,v in dict.items():
#    sum+=int(v)
#print("total cobfirmed",sum)
for k,v in dict.items():
    clist.append(int(v))
for k,v in dict.items():
    if(max(clist)==int(v)):
        print("\n highest confirmedrate:",k,v)