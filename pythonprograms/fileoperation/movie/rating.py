f=open("movies.csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    ratingwise=data[3]
    movie=data[1]
    if ratingwise not in dict:
        dict[ratingwise]=1

    else:
        dict[ratingwise]+=1


for k, v in dict.items():
   print("\n Ratingwise count:",k,"movies",v)