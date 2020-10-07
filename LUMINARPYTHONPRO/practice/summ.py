list=[10,40,3,6,8,2]
ele=int(input("Enter the num"))
low=0
upp=len(list)-1
list.sort()
while(low<=upp):
    data=list[low]+list[upp]
    if(data==ele):
        print("pairs are:", list[low], ",", list[upp])

    elif(data>ele):
        upp=upp-1
    else:
        low = low + 1

