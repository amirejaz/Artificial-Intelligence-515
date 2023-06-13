# >>> help(dict.get)
# Help on method_descriptor:

# get(self, key, default=None, /)
#     Return the value for key if key is in the dictionary, else default.
dict1 = {
    "Name" : "Amir Aijaz",
    "Age" : 21,
    "Occupation" : "Data Scientist"
}
print(dict1.get("Name"))