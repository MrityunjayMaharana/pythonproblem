roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
u=[]
for i in roll_number:
    if i not in sample_dict:
        roll_number.remove(i)
        u.append(i)
print("Unwanted list:",u)
print("After removing : ",roll_number)