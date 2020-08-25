employee={"id":1001,"name":"arjun","designation":"developer","salary":15000}
print(employee["name"])
print("company" in employee)
employee["company"]="LUMINAR"
print(employee)
employee["salary"]+=35000
print(employee)
for key in employee:
  print(key,",",employee[key])