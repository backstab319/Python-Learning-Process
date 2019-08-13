list1 = ["Good","Bad","Good","Bad","Good","Bad","Good","Bad"]
dict1 = {}
temp = {}
for i,j in enumerate(list1):
    print(i,j)
    num = list1.count(j)
    temp = [j]
    dict1 = dict1.items() + num
print(dict1)