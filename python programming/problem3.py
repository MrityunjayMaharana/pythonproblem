sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
def chunk(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
a=list(chunk(sample_list,3))

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
for i in a:
    print(i)
    print("After reversing : ",i[::-1])