f=open("coviddet","r")

dictt={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmedcases=data[4]
   # print(state,",",confirmedcases)
    if state not in dictt:

        dictt[state] = confirmedcases
    else:

        dictt[state] = confirmedcases

for l, m in dictt.items():
    print(l, ",", m)