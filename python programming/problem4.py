sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
u=[]
for i in sample_list:
    a=sample_list.count(i)
    u.append(a)
b=zip(sample_list,u)
print("Printing occurence of each item : ",dict(b))