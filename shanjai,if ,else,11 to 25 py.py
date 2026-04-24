'''#11
num1=int(input())
num2=int(input())
differ=num1-num2
if(differ==0):
    print("The difference is 0")
else:
    print("The difference is not 0")
'''
'''#12
mark=int(input("Enter Mark:"))
if(mark>=50 and mark<=100):
         print("Passed")
elif(mark<50):
    print("Fail")
else:
    print("Invalid Input")
'''
'''#13
num=int(input("Enter number:"))
if(num%10==0):
        print("yes")
else:
    print("No")
'''
'''#14
num=int(input("Enter number two digit:"))
o=num//10
e=num%10
if(o>e):
        print("Biggest digit :",o)
else:
    print("Biggest digit:",e)
'''
'''#15
choice=int(input("give Choice:"))
if(choice==1):
    print("The exam will be easy")
elif(choice==2):
    print("The exam will be difficult")
else:
    print("Invalid Input")
'''
'''#16
value=int(input("Enter number(1 or 2) :"))
if(value==1):
    print("Youcan go out and play")
elif(value==2):
    print("You cannot go out and play")
else:
    print("Ivalid input")
'''
'''#17
length=float(input("Enter the value :"))
breadth=float (input("Enter the value :"))
if(length==breadth):
    print("Square")
else:
    print("Rectangle")
'''
'''#18
num=int(input("Enter the value :"))
if(num>=65 and num<=90):
    print("It is ASCII value in Uppercase alphabet ")
else:
    print("It is not ASCII value in uppercase alphabet")
'''
'''#19
num=int(input("Enter number:"))
if(num>=97 and num<=122):
    print("It is ASCII value in lowercase alphabet")
else:
    print("It is not ASCII value in lowercase alphabet")
'''
'''#20
num=int(input("enter the number :"))
if(num>=48 and num<=57):
   print("It is ASCII value in numeric character")
else:
    print("It is not ASCII value in numeric character")
'''
'''#21
num=int(input("Enter the number:"))
if(num%5==0 and num%3==0):
    print("It is Multiple by both 5,3")
else:
    print("Not multiple ")
'''
'''#22
num=int(input("Enter the number :"))
if(num>=100 and num<=999) or (num>=-100 and num<=-999):
     if(num%10==0):
         print("It is Three digit number and Multiple by 10")
     else:
         print("It is Three digit number not multiple by 10")
else:
    print("Invalid input")
'''
'''#23
num=int(input("Enter the number:"))
if(num>=100 and num<=999) or (num>=-100 and num<=-999):
    if(num%2==0 and num%5==0 and num%10==0):
        print("It is three digit and multiple by 2,3,10")
    else:
         print("It is three digit and not multiple by 2,5,10")
else:
    print("Not Three Digit and NOT multiple by 2,5,10")
'''
'''#24
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
if(num1%2==0 and num2%2==0):
    print("The product is :",num1 * num2)
else:
    print("The sum is:",num1 + num2)
'''
'''#25
num=int(input("Enter the number:"))
if (num%10==7 or num%7==0):
    print(num,"this is Buzz number")
else:
    print(num,"this is not Buzz number")
'''



































































