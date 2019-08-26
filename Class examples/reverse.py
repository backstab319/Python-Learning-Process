inp,rev = input("Enter a string or number "),""
i=len(inp)-1
while i >= 0:
    rev+=inp[i]
    i-=1
print(rev)