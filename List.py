#22.122019

>>> word = 'Programming'
>>> word[0]
'P'
>>> word[-2]
'n'
>>> word[3:5]
'gr'
>>> word[4:9]
'rammi'
>>> word[:5]
'Progr'
>>> word[8:]
'ing'
>>> word[5:-3]
'amm'
>>> word[:2] + word[3:]
'Prgramming'
>>> len(word)
11
>>> square = 'Square'
>>> len(square)
6
>>> len(word) + len(square)
17
>>> cube = [10, 20, 30, 45, 50]
>>> cube
[10, 20, 30, 45, 50]
>>> cube[3] = 40
>>> cube
[10, 20, 30, 40, 50]
>>> cube[5] = 60
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> cube.append(60)
>>> cube.append(4+10+20+36)
>>> cube
[10, 20, 30, 40, 50, 60, 70]
>>> programA = ['A','B','C','D','E']
>>> programB = ['a','b','c','d','e']
>>> programC = programA + programB
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> programD = [1, 2, 3, 4, 5]
>>> programC = programC + programD
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
>>> len(programC0
... len(programC)
  File "<stdin>", line 2
    len(programC)
      ^
SyntaxError: invalid syntax
>>> programC[9:] = []
>>> programC[5:9] = programD
>>> programC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]
>>> len(programC)
10
>>> a = [10, 20, 30, 40, 50]
>>> b = [60, 70, 80, 90, 100]
>>> c = [110, 120, 130, 140, 150]
>>> x = [a,b,c]
>>> x
[[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
>>> x[0][]
  File "<stdin>", line 1
    x[0][]
         ^
SyntaxError: invalid syntax
>>> x[][3]
  File "<stdin>", line 1
    x[][3]
      ^
SyntaxError: invalid syntax
>>> x[1][2]
80
>>> x[][]
  File "<stdin>", line 1
    x[][]
      ^
SyntaxError: invalid syntax
>>> x[0][0]
10
>>> x[1][1]
70
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
>>> x[1][2] + x[2][0]
190
>>> x[0][1] - x[2][1]
-100
>>> if else Statement (While)
  File "<stdin>", line 1
    if else Statement (While)
          ^
SyntaxError: invalid syntax
>>> If else Statement (While)
  File "<stdin>", line 1
    If else Statement (While)
          ^
SyntaxError: invalid syntax
>>>


