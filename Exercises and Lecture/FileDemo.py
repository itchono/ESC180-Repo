fname = 'LeagueItemsDataTest.txt'
# specify filename

items = open(fname, 'r') # 'r' is important, not just the unchar'd letter lol

arr = list(items)

for i in range(0, len(arr)):
    arr[i] = arr[i].strip("\n")

arr.sort()
print(arr)

items.close()

# writing part

champs = open('champs_I_dont_like.txt', 'w')

for i in range(0, 100):
    champs.write(" "*(50-int(i/2)) + "B"*i + "\n")

champs.close()
