list=[]
n=int(input("Enter the limit"))
print("Enter the numbers:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("Elements in list",list)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(list[j]>list[j+1]):
            swap=list[j]
            list[j]=list[j+1]
            list[j+1]=swap
            print(list)
        else:
            print(list)
    print()
print("Sorted element in list are:",list)
