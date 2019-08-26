series,total = input("Enter a series of numbers to find their average ").split(),0
for i in series: total+=int(i)
print("Average of the series is",total/len(series))