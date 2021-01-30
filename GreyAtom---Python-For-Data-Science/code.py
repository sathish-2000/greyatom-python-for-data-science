# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2

# Append the list
new_class.append('Peter Warden')
# Print updated list
print (new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print (new_class)


# Create the Dictionary
courses = {'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60 }


# Slice the dict and stores  the all subjects marks in variable

# Store the all the subject in one variable `Total`
total = (courses.get('Math') + courses.get('English') + courses.get('History') + courses.get('French') + courses.get('Science'))
# Print the total
print (total)
# Insert percentage formula
percentage = 100.0 * total / 500
# Print the percentage
print (percentage)



# Create the Dictionary
mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65,
'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}

topper = max(mathematics,key = mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
# Code starts here

last_name = topper.split()[1]
first_name = topper.split()[0]

full_name = last_name + " " + first_name

certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


