# Program that reads in a 10 character bank number and outputs the last 4 digits with X's replacing the rest of the leading digits
# Author Niall Madden

bankaccountNumber = input("enter your bank number")
secureoutput = bankaccountNumber[-4:].rjust(len(bankaccountNumber),'X')

print(secureoutput)
