def fact(n):
  x = 1

  if n <= -1:
        print("enter value is invalid ")
        print("PLEASE RECHECK THE GIVEN VALUE")
  elif n==0:
      print("1")
  elif n>=101:
      print("the program is ment only below 100 factiorals")
  else:
    for i in range(1, n+1):
     x = x*i
    return x


x = int(input("enter the value of n : "))
y = fact(x)


def fact(a):

  x = 1

  if a <= -1:
        print("enter value is invalid ")
        print("PLEASE RECHECK THE GIVEN VALUE")
  elif a==0:
      print("1")
  elif a>=101:
      print("the program is ment only below 100 factiorals")
  else:
    for i in range(1, a+1):
     x = x*i
    return x


p = int(input("enter the value of n : "))
q = fact(p)

print("1,add")
print("2,subract")
print("3,mult")
print("4,div")
z=int(input("enter required function 1,2,3,4 : "))
if z==1:
    e=y+q
    print("the addition of ",x,"! and",p,"! is",e)
elif z==2:
   if y<<q:
    y,q=q,y
    s=y-q
    print("the substraction of",x,"! and",q,"! is",s)
elif z==3:
    m=y*q
    print("the mult of",x,"! and",p,"! is",m)
elif z==4:
     d=y/q
     print("the div of",x,"! and",p,"! is",d)
else:
    print("the program is only ment for above 4 function")