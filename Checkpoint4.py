#upload to Git

#Leslie W. Checkpoint 4

#Exercise 1: 	Create a -

#list
start_list  = [1, 2, 3, 4]
print(start_list)
#tuple
start_tuple = ('red', 'blue', 'green')
print(start_tuple)
#float 
start_float = 1.2
print(start_float)
#integer 
start_integer = 20
print(start_integer)
#decimal 
from decimal import Decimal
start_decimal = Decimal(1.05)
print(start_decimal)
#dictionary
start_dictionary = {
    "water" : "Squirtle",
    "fire" : "Charmander",
    "grass" : "Venusar",
}
print(start_dictionary)

#Exercise 2: 	Round your float up.
import math

print(math.ceil(start_float))
#Exercise 3: 	Get the square root of your float.

print(math.sqrt(start_float))
#Exercise 4: 	Select the first element from your dictionary and print it out..

print(list(start_dictionary.items())[0][1])

#Exercise 5: 	Select the second element from your tuple.
element_2 = start_tuple[0]
print(element_2)
#Exercise 6: 	Add an element to the end of your list.
start_list.append(10)
print(start_list)
#Exercise 7: 	Replace the first element in your list.
start_list[0] = 20
print(start_list)
#Exercise 8: 	Sort your list alphabetically.
list_abc_sort = start_list.sort()
print(start_list)
#Exercise 9: 	Use reassignment to add an element to your tuple.
purple = 'purple'
start_tuple += (purple,)
print(start_tuple)
#Exercise 10: 	Using the following list, reorder the elements so that they are arrayed in reverse alphabetical order.
my_list = ['mars', 'earth', 'venus', 'pluto', 'saturn']
reverse_sorted_list = sorted(my_list, reverse=True)
print(reverse_sorted_list)
