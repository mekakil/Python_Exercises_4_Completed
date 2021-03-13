"""
@Author:Victor Hugo de Barros
"""

# Flag receive ''False'' already, and under FOR  it set that ''Flag'' receives
# ''Flag'' that's is already set as ''False'' or ''c.islower function'' which can
#be FALSE or TRUE itself. So, it is a syntax error.


def any_lowecase4(s):
  flag = False # ---> determine a status beforehand the verification.
  for c in s:
    flag = flag or c.islower():  #----> flag variable receives another two reductant items(variable and a function). 
  return flag
      
print(any_lowecase4('C'))
#SyntaxError: invalid syntax
