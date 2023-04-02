list_values = [1, 2, "Three", 4.0, 'Five']
print(list_values)
print(list_values[2])
print(list_values[-1])
print(list_values[-2])
print(list_values[0:-1]) #prints [1, 2, 'Three', 4.0] and not the last item

list_values.insert(2, 2.5)
print(list_values)

list_values.append(6.0)
print(list_values)

list_values[1] = 'Two'
print(list_values)

del list_values[2] # Deletes the referred value in the list
print(list_values)

list_values.append("Last")
print(list_values)

del list_values #Deletes the entire list

print("####################################################################################")
tuple_values = (1, 2, "Three", 4.0, 'Five', 2)
print(tuple_values)
print(tuple_values[2])
print(tuple_values[-1])
print(tuple_values[-2])
print(tuple_values[0:-1]) #prints [1, 2, 'Three', 4.0] and not the last item

# Below assignment not allowed and will throw TypeError: 'tuple' object does not support item assignment
#tuple_values[0] = 'One'

print(tuple_values.count(2)) #returns the number of occurrences of the values specified in the tuple

print(tuple_values.index("Five"))
print("####################################################################################")

dict_values = {1 : "fname", 2 : 'lname', "c" : 3, 'd': 4.0}
print(dict_values)
print(dict_values[2])
print(dict_values["d"])

dict_values1 = {}
dict_values1[5] = 'mname'
print(dict_values1)

"""
print(tuple_values[2])
print(tuple_values[-1])
print(tuple_values[-2])
print(tuple_values[0:-1]) #prints [1, 2, 'Three', 4.0] and not the last item
"""