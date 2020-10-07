import functools
lst=[25,20,30,31,32]
#sum=functools.reduce(lambda num1,num2:num1+num2,lst)
#print(sum)
#maxval=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
#print(maxval)
minval=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(minval)