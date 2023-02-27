# Program that reads a string and strips any leading or trailling spaces
# author niall madden

rawstring = input("enter a string")
normalisedString = rawstring.strip().lower()

lengthofRawstring = len(rawstring)
lengthofNormalisedString = len(normalisedString)

print (f"the string normalised is :{normalisedString}")
print(f"we reduced the string from {lengthofRawstring} to {lengthofNormalisedString} characters")
