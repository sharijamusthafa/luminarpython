f=open("empp","r")
emp={}
for lines in f:
    id,name,des,sal=lines.rstrip("\n").split(",")
    if(id not in emp):
        emp[id]={"id":id,"name":name,"des":des,"salary":sal}
print(emp)
def fetchData(**kwargs):
    id=kwargs["id"]

    if(id not in emp):
        print("employee not exit")
    else:
        print(emp[id]["name"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])

#fetchData(id="1001")
fetchData(id="1001",prop="salary")