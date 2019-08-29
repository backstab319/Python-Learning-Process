li = [1,2,3,4,5,6,7,8,9,10]
even = {i:i**3 for i in li if i%2== 0}

# for i in li:
#     if i%2 == 0:
#         even[i] = i**3
# print(even)

# a = [1,2,3,4,5,6]
# b = [3,4,5]
# c = {}
# c = {i:j for i,j in zip(a,b)}
# for i,j in zip(a,b):
#     c[i] = j
# print(c)

a = [1,2]
b = [3,4]
c=[]
for i,j in a,b: c+=[i],[j]
print(c)
for i in c:
    for j in i:
        print(j)