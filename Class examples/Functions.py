list1 = []
def list_append(data,code):
    if code == 0: list1.append(data)
    else: print(list1)

for i in range(3):
    x = input("Enter some data to append ")
    list_append(x,0)
list_append(None,1)