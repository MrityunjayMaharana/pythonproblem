first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
a=first_set.intersection(second_set)
print("Intersection is : ",a)
first_set-=second_set
print("After removing common element : ",first_set)