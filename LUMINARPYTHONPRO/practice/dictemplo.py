employee={"id":100,"name":"shaani","des":"tester","salary":10000}
print(employee["name"])
employee["salary"]+=10000
print(employee)
employee["company"]="luminar"
print(employee)
for key in employee:
    print(key,",",employee[key])