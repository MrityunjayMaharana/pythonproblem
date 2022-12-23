l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
u=[]
v=[]
for i in range (0,len(l1)):
    if i%2 != 0:
        a=l1[i]
        u.append(a)
for j in range (0,len(l2)):
    if j%2 == 0:
        b=l2[j]
        v.append(b)
print("Element at odd-index positions from list one:")
print(u)
print("Element at even-index positions from list two :")
print(v)
print(u+v)