import re
# x = re.compile("python")
# print(type(x))

# x = re.compile("ab")
# matcher = x.finditer("abababaaaabbbbab")
# count = 0
# for match in matcher:
#     count+=1
# print(count)

# inp = ["[abc]","[^abc]","[a-z]","[A-Z]","[a-z A-Z]","[0-9]","[a-z A-Z 0-9]","[^a-z A-Z 0-9]"]
# for i in inp:
#     print("For expression",i)
#     matcher = re.finditer(i,"abc@89Hi")
#     for match in matcher:
#         print(match.start(),match.group())

# inp = ["[\s]","[\S]","[\d]","[\D]","[\w]","[\W]","."]
# for i in inp:
#     print("For expression",i)
#     matcher = re.finditer(i,"ABb @9hz* K")
#     for match in matcher:
#         print(match.start(),match.group())

inp = ["a","a+","[a*]","a?","a{1}","a{1,3}","[^a]","^a","a$"]
for i in inp:
    print("For expression",i)
    matcher = re.finditer(i,"ABb @9hz* a K")
    for match in matcher:
        print(match.start(),match.group())