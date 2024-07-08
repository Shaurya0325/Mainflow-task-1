# Creating a list
fruits = ['apple', 'banana', 'cherry']
print("List:", fruits)
    
# Modifying list
fruits[1] = 'orange'
print("Modified List:", fruits)
    
# Adding to list
fruits.append('pear')
print("List after adding 'pear':", fruits)
    
# Removing from list
fruits.remove('apple')
print("List after removing 'apple':", fruits)
    
print("\n")
    
 # Creating a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:", person)
    
# Modifying dictionary
person['age'] = 31
print("Modified Dictionary:", person)
    
# Adding to dictionary
person['job'] = 'Engineer'
print("Dictionary after adding 'job':", person)
    
# Removing from dictionary
del person['city']
print("Dictionary after removing 'city':", person)
    
print("\n")
    
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
print("Set:", unique_numbers)
    
# Adding to set
unique_numbers.add(6)
print("Set after adding '6':", unique_numbers)
    
# Removing from set
unique_numbers.remove(3)
print("Set after removing '3':", unique_numbers)
    
# Modifying set
unique_numbers.discard(1)
unique_numbers.add(11)
print("updated set:",unique_numbers)
    
print("\n")