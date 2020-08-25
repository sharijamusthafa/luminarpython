f=open("covid_19_india.csv","r")
dict={}
dlist=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
   # print(state,",",deathcount)
    if state not in dict:
        dict[state]=death
    else:
        dict[state]=death
#sum=0
#for k,v in dict.items():
 #   sum+=int(v)
#print("total death",sum)
for k,v in dict.items():
    dlist.append(int(v))
for k,v in dict.items():
    if(max(dlist)==int(v)):
        print("\n highest deathrate:",k,v)



