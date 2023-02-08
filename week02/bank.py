# bank.py
# author: Niall Madden

# Input
Amount1 = int(input("Enter amount 1 (in cents)"))
Amount2 = int(input("Enter amount 2 (in cents)"))
sum = float((Amount1+Amount2)/100)
print("The sum of these is ${:,.2f}".format(sum))
