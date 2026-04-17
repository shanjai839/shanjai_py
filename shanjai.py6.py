#swapping using third variable

a=int(input("Enter values of a:"))
b=int(input("Enter values Of b:"))

print("Before swapping:")
print("a:",a)
print("b:",b)

x=a
a=b
b=x

print("After swapping:")
print("a:",a)
print("b:",b)



#swapping using without third variable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

print("Before swapping:")
print("a:",a)
print("b:",b)

a,b=b,a  #swap

print("After swapping:")
print("a:",a)
print("b:",b)

    
      
