list=[1,2,3]
ele=int(input("Enter the num:"))
low=0
upp=len(list)-1
list.sort()
while(low<=upp):
    data=list[low]+list[upp]
    if(data==ele):
        print("pairs are:", list[low], ",", list[upp])
        break
    elif(data>ele):
        upp=upp-1
    else:
        low = low + 1