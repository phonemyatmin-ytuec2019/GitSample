#21.12.2019


>>> 2 + 2     
4
>>> 50 - 5 * 6
20
>>> (50- 5 * 6) / 4    
5.0
>>> round(5.0)          # removing the decimal
5
>>> 17 / 3
5.666666666666667
>>> 5.123456
5.123456
>>> round(5.123456,2)   # placing the decimal to 2 places
5.12
>>> 17 // 3             # quotient
5
>>> 18 // 4
4
>>> 20 // 5
4
>>> 17 % 3              # remainder
2
>>> 17 * 4 % 3          # operator priority
2
>>> 3 ** 2              # 3 to the power of 2
9
>>> 3 ** 9
19683
>>> 7 ** 3
343

a = 1
a (variable) = (assign) 1 (value)

width = 20 
height = 5 * 9
vol = width * height
vol

sale = 30000
tax = 5 / 100
total_tax = sale * tax
total_tax
total_price = sale + total_tax
total_price


>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'

>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.


print("""\
Usage: thingy
		-a
		-b
		-c
""")

"""...""" or '''...'''

3 * 'A'
2 * 'BC' + 'DE'
10 * 'GH' + 3

word = 'Programming'
word[0]
word[-2]
word[3:5]    # from 3 to 5
word[4:9]
word[:5]
word[8:] 
word[5:-3]
word[:2] + word[3:]