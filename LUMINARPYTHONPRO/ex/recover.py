f=open("coviddet","r")
dict={}
for lines in f:
    date,state,Latitude,Longitude,confirmedcases,death,cured,Newcases,ndeaths,nrecovered=lines.rstrip("\n").split(",")
    if (state not in dict):
        dict[state] = {"state": state,"confirmedcases":confirmedcases,"death":death,"cured":cured,"Newcases":Newcases,"ndeaths":ndeaths,"nrecovered":nrecovered}
    #print(dict)
def fetchData(**kwargs):
    id=kwargs["state"]

    if(state not in dict):
        print("state not exit")
    else:
        print(dict[state]["nrecovered"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(dict[state][val])


fetchData(state="Kerala",prop="nrecovered")