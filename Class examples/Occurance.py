list1 = ["sid","sid","Good","Bad","Good","Bad","google","Bad","Good","Good","sid","sid","crab","google"]
dict1 = {}
i = 0
while list1:
    val = list1[0]
    count = list1.count(val)
    temp = {count:val}
    dict1.update(temp)
    while val in list1: list1.remove(val)
    i+=1
print(dict1)