# program prints out random fruit names
# author niall madden

import random
fruits = ['Apple', 'Banana', 'Pomegranite', 'Orange', 'Pear']
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit is:{}".format(fruit))