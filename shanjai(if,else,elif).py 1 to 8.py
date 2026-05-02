'''#1
a=int(input("enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))
if(a>=b and a>=c):
    print("Largest number:",a)
elif(b>=a and b>=c):
    print("Largest number:",b)
elif(c>=a and c>=b):
    print("Largest number:",c)
else:
    print("Invalid Input")
'''
'''#2
a=int(input("Enter the number 1:"))
b=int(input("Enter the numbet 2:"))
c=int(input("Enter the number 3:"))
if(a<=b and a<=c):
    print("Smallest number :",a)
elif(b<=a and b<=c):
    print("Smallest number :",b)
elif(c<=a and c<=b):
    print("Smallest number :",c)
else:
    print("Invalid input")
'''
'''#3
num=int(input("Enter the number:"))
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")
'''
'''#4
days=int(input("Entrer no days:"))
if(1<=days<=5):
    print("Fine amount:",days*40)
elif(6<=days<=10):
    print("Fine amount:",days*65)
elif(10<days):
    print("Fine amount:",days*80)
'''
'''#5
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
operation=str(input("Enter operation (add,sub,mult,div):"))
if(operation=="add"):
    print("Add value:",num1+num2)
elif(operation=="sub"):
    print("sub value:",num1-num2)
elif(operation=="div"):
    print("Div value:",num1/num2)
elif(operation=="mult"):
    print("Mult value:",num1*num2)
else:
    print("Invalid input")
'''
'''#6
num=int(input("Enter the number:"))
if(num%5==0 and num%3==0 and num%7==0):
    print("Yes Multiple")
else:
   print("Not Multiple")
'''
'''#7
weight=int(input("Enter the weight :"))
speed=str(input("Enter the type(o or E):"))
if(0<weight<=100):
    if(speed=="o"):
        print("Charge:100 for the weight",weight)
    else:
        print("Charge:80 for the weight",weight)
elif(weight>=101 and weight<=500):
    if(speed=="o"):
        print("Charge:200 for the weight",weight)
    else:
         print("Charge:150 for the weight",weight)
elif(weight>=501 and weight<=1000):
    if(speed=="o"):
        print("Charge:250  for the weight",weight)
    else:
         print("Charge:210 for the weight",weight)
elif(weight>1000):
    if(speed=="o"):
        print("Charge:300 for the weight",weight)
    else:
         print("Charge:250 for the weight",weight)

'''
'''#8
rate=int(input("Enter rate:"))
if(rate<=50000):
    print("price of laptop:",rate)
    print("Discount:",(rate*0)/100)
    print("Total price:",rate-(rate*0)/100)
elif(50001<=rate<=100000):
    print("Price of laptop:",rate)
    print("Discount:",(rate*10)/100)
    print("Total price:",rate-(rate*10)/100)
elif(100001<=rate<=150000):
    print("Price of laptop:",rate)
    print("Discount:",(rate*15)/100)
    print("Total price:",rate-(rate*15)/100)
elif(rate>=150000):
    print("Price of laptop:",rate)
    print("Discount:",(rate*20)/100)
    print("Total price:",rate-(rate*20)/100)
else:
    print("invalid input")
'''


















































              




              
