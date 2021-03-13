"""
@Author:Victor Hugo de Barros
"""

#The function takes ''c'' as true and 'C' as False,
#and that's exaclty how it prints out.
# I coun't identify any error.

def any_lowecase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False

print(any_lowecase1('Comida'))
#False

print(any_lowecase1('comida'))
#True

print(any_lowecase1('cOMIDA'))
#False