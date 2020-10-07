f=open("coviddet","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    recov=data[6]
    confirm=data[4]
    death=data[5]
    if (state not in dict):
        dict[state] = {"state": state,"confirmedcases":confirm,"death":death,"recovered":recov}
    else:
        dict[state] = {"state": state, "confirmedcases": confirm,"death":death,"recovered":recov}
    #print(dict)
def fetchData(**args):
    id=args["state"]
    if(id not in dict):
        print("error")
    else:
        for k, v in dict.items():
            if(k==id):
                print("state=",id,",","confirmd=",v["confirmedcases"])
                if("prop" in args):
                    kk=args["prop"]
                    if(kk=="recov"):
                        #print("state=",id,",","recv=",v["recovered"])
                         print("state=",id)
                         print(dict[id]["recovered"])
                    elif(kk=="death"):
                        print("deathh=",v["death"])



fetchData(state="Kerala",prop="recov")