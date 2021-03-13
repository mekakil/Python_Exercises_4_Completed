"""
@Author:Victor Hugo de Barros
"""
import math

def my_sqrt(a):
    x = 3
    y = 1
    opsilon =  0.00001
    while True:
        print(x)
        y = (x+ a/x) / 2
        if abs(y-x) < opsilon:
          break
        x = y
        return x

def test_square_root():
    a = 1.0
    x=' ';
    print('a' + 10*x + 20*x + 'my_sqrt' + 10*x + 20*x + 'math.sqrt' + repr(my_sqrt(a)).rjust(6),+10*x + 5*x + 'Diff' +repr(math.sqrt(a)).rjust(12) + 'diff'.rjust(10))
    print("-      ---------             ------------                         -----------                        -----------")
    while a < 26.0:
        print(a,+10*x + 5*x , my_sqrt(a),+10*x + 5*x , math.sqrt(a),+10*x + 5*x , abs(my_sqrt(a)-math.sqrt(a)))
        a += 1

test_square_root()



"""
Think Python 2nd Edition Exercise 7-1. (2017).Stackoverflow. https://stackoverflow.com/questions/54524026/recursive-square-root-loop-in-python-with-a-epsilon-of-0001
"""