#!/usr/bin/env python3
number_of_factors = 3
summ = 0

for x in range(0, number_of_factors):
   import math
   print('Enter the number {0:d} of {1:d}:'.format(x, number_of_factors))
   summ = summ + input()

print ("The summ is:{0:d}".format(summ))


