# convert float to int taking dollars & cents and convert to cents
# author Niall Madden

amount = float(input("Enter amount in dollar & cents"))
amountincents = int(amount*100)

print("total in cents is {}".format(amountincents))