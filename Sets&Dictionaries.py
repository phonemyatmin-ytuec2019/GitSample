#Sets

#includes a data type for sets
#Curly braces or the set() function can be used to create sets


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # show only one of the duplicated ones


'orange' in basket
'crabgrass' in basket # fast membership testing



# Demonstrates set operations on unique letters from two words


a = set('abracadabra')
b = set('alacazam')
a 			#unique letters in a
a - b    	#letters in a but not in b
a | b 		#letters in a or b or in both
a & b 		#letters in both a and b
a ^ b 		#letters in a or b but not both



a = {x for x in 'abracadabra' if x not in 'abc'}
a


------

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)


fruits.add("cucumber")  #add the string as a whole 
fruits
fruits.update("grape", "water melon") #add the string in separate char values
fruits
fruits.remove("banana") #remove the string
fruits
fruits.discard("kiwi") #remove the string
fruits



>>>Dictionaries



#Dictionaries

#Another useful data type built into python is the dictionary


tel = {'jack' : 4098, 'sape' : 4139} # {'index' : value}
tel['guido'] = 4127 
tel

tel[0] # can't use

tel['jack'] #call teh index to show value


del tel['sape'] # deletes the index value of sape
tel['irv'] = 4127
tel


list(tel)	#print only index

sorted(tel)	#sorting the index


dict([('sape', 4139), ('guido', 4137), ('jack', 4098)])	# converting into dict type
dict(sape = 4139, guido = 4137, jack = 4098) # same as above


{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k,v)




for i,v in enumerate(['tic', 'tac', 'toe']):  # genrate list numbers
	print(i,v)  



questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
	print('What is your {0} It is {1}.'.format(q,a))