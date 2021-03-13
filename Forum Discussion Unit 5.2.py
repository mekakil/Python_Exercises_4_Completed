"""
@Author:Victor Hugo de Barros
"""
#The 'c' object is given as a string and the Boolean Expressions also marked as a string
# not effectively executing their purpose.

def any_lowecase2(s):
  for c in s:
    if 'c'.islower():  #<--- the "c"" us being check by 'for c in s:". It return true for all arguments.
      return 'True'
    else:
      return 'False'

print(any_lowecase2('Comida'))
#True

print(any_lowecase2('comida'))
#True