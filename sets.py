my_set={1,2,2,2,3,3,4,4,5,6,6,6}
print(my_set)

set1 = my_set
set2 = {1,5,8,9,7}
print("Difference between both sets:")
print(set1.difference(set2))
print("Symmetric difference:")
print(set1.symmetric_difference(set2))