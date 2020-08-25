n=int(input("enter the integer:"))
rev=0
original=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n//=10
if(original==rev):
    print(rev,"is palindrome")
else:
    print(rev,"is not palindrome")