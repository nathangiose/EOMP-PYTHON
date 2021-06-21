# Nathan John Giose
# Importing random data


'''''
import random


# Now I will create a variable for the lotto numbers


my_lotto = []
for x in range(6):
    x = random.randint(1, 50)
    my_lotto.append(x)
    my_lotto.sort()

# Do not add the print in the same loop


print("Your lotto numbers are as follows: ")
print(my_lotto)
'''''

import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,49)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead
    number = random.randint(1,49)

  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()

#Display the list on screen:
print(">>> Today's lottery numbers are: ")
print(lotteryNumbers)


