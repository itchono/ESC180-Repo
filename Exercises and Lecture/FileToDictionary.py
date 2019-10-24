fname = 'LeagueItemsDict.txt'
fwrite = 'LeagueItemsAvg.txt'

items = open(fname, 'r')
write = open(fwrite, 'w')

lines = list(items)

d = {'Berserker\'s Greaves':{'Cost':1100, 'Tier':"Advanced", 'Winrates':[49, 50, 51,52]}}


columns = lines[0].strip("\n").split("\t") # tab delimited values


for i in range(1, len(lines)):
    currline = lines[i].strip("\n").split("\t")
    d[currline[0]] = {} # empty dict

    for j in range(1, len(currline)):
        if j < 3:
            d[currline[0]][columns[j]] = currline[j]
        else:
            d[currline[0]][columns[j]] = currline[j].strip().split(",")


print(d)

write.write(lines[0])

for key in d.keys():
    write.write(key + "\t")
    for subkey in d[key].keys():
        s = 0
        if type(d[key][subkey]) != type([]):
            write.write(str(d[key][subkey]) + "\t")
        else:
            for i in d[key][subkey]:
                write.write(str(i) + ",")
                s += int(i)
            write.write(str(s/len(d[key]['Winrates'])))
                
    write.write("\n")
    
    

items.close()
write.close()
