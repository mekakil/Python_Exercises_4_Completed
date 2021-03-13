
"""
@Author:Victor Hugo de Barros
"""

#The function any-lowercase5() has two alternative exercution:
# the one if the letter not being a lowercase then is 'False''
# otherwise it is ''True''.

def any_lowecase5(s):
  for c in s:
    if not c.islower():
      return False
    else:
      return True

print(any_lowecase5('Comida'))
#False

print(any_lowecase5('comida'))
#True
