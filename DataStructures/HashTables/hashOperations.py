# =============================   HASH TABLES / HASH MAP   ============================= #
#
#
# HASH TABLES OR HASH MAP is a DS that maps the key to its value pair i.e stores data in key-value pair
##
# We can create hash tables using builtin dict() or by using curly braces#

my_dict = {
    'name': 'Sonam',
    'ID': '003'
}

builtin_dict = dict(Sonam='002', Resham='003')
# print(builtin_dict)

# Nested dictionaries
emp_details={'Employee': {'Sonam': {'ID': '001', 'Salary': '2000'}, 'Resham': {'ID': '002', 'Salary': '1000'}}}
# print(emp_details)

# OPERATIONS =====>>>>

#
# Accessing Items #
my_dict['name']
# print(my_dict)
# using keys and values function accessing
print(my_dict.keys())
print(my_dict.values())

#using get()
print(my_dict.get('name'))

# Get all keys
for i in my_dict.values():
    print(i)

# Get the data in key value pairs
for i, j in my_dict.items():
    print(i, j)

#------------------------------------------------------------#

# Updating Items #

my_dict['ID'] = '001'
my_dict['age'] = '25'
print(my_dict)

#------------------------------------------------------------#

# Deleting Items #

# my_dict.pop('age')
# print(my_dict)

# popItem() =====>>>> remove last inserted value
my_dict.popitem()
print(my_dict)

# Using del keyword
del my_dict['ID']
print(my_dict)


#------------------------------------------------------------#

# Converting dictionary into Dataframes #

import pandas as pd 

df = pd.DataFrame(emp_details)
print(df)