f=open("temperaturedata","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    dis=data[0]
    tem=data[1]
    print(dis)
    print(tem)
    if(dis not in dict):
        dict[dis]=tem
    else:
        old=dict[dis]
        if(tem>old):
            dict[dis]=tem
print(dict)

