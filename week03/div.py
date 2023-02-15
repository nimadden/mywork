# program to divide 2 numbers and outputs integer answer with remainder
# author : Niall Madden

x = int(input("enter first number"))
y = int(input("enter second number"))
answer = int(x//y)
remainder = int(x%y)

print("{} divided by {} equals {} with a remainder of {}".format(x,y,answer,remainder))