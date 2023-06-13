List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
lst2 = []

indices_to_remove = [0, 4, 5]
for i in range(len(List)):
    if i not in indices_to_remove:
        lst2.append(List[i])

print(lst2)
