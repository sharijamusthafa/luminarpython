student={"ro":1002,"name":"tinu","age":25,"cp":26}
print(student["name"])
print(student["cp"])
for key in student:
    print(key,",",student[key])
student["cp"]+=5
print(student)
#print("total" in student)
student["total"]=17
print(student)