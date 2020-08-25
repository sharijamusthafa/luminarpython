list=[1,2,3,4,5]
sq=[(i*i) for i in list]
print(sq)

pairs=[(i,j) for i in list for j in list]
print(pairs)

odd=[i for i in list if i%2!=0]
print(odd)


odd=[i for i in list True if i%2!=0 else False]
print(odd)