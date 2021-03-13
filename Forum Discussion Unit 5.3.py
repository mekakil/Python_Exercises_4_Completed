"""
@Author:Victor Hugo de Barros
"""

#THe function is not well set because when inserted a Uppercase at
# the end it not recognize and returns ''True''.

def any_lowecase3(s):
  for c in s:
    flag = c.islower()
    return flag
    
print(any_lowecase3('cComCidC'))
#True
print(any_lowecase3('comida'))
#True
print(any_lowecase3('Comida'))
#False