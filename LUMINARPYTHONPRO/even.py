low=int(input("enter lowerlimit"))
upper=int(input("enter upper limit"))
flag=1
for num in range(low, upper + 1):
  if(num>1):
      for i in range(2,num):
          if(num%i==0):
              flag = 0
              break
          else:
              flag = 1
      if (flag > 0):
          print("prime no.",num)
      else:
          print("nonprime",num)


