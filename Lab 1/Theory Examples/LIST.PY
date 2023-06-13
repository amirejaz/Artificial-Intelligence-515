fruits = ['apple','orange','pear','banana']
print(fruits[0])

# We can use the + operator to do list concatenation:
otherFruits = ['kiwi','strawberry']
print(fruits + otherFruits)

# Python also allows negative-indexing from the back of the list. For instance, fruits[-1] will access the
# last element 'banana':
fruits[-2] = 'pear'
print(fruits.pop())
print(fruits)

fruits.append('grapefruit')
print(fruits)

fruits[-1] = 'pineapple'
print(fruits) 

# We can also index multiple adjacent elements using the slice operator.
print(fruits[0:2])

print(fruits[:3])

print(fruits[2:])
 
print(len(fruits))

# The items stored in lists can be any Python data type. So for instance we can have lists of lists:
lstOfLsts = [['a','b','c'],[1,2,3],['one','two','three']]
print(lstOfLsts[1][2])
print(lstOfLsts[0].pop())
