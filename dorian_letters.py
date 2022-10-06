file = open("dorian.txt", 'r')
locc = {} # dictionary for occurrences of letters
for line in file: # read file line by line
    line = line.strip().lower()
    for l in line: # read line char by char
        if l not in locc:
            locc[l] = 1
        else:
            locc[l] += 1
file.close()
rlocc = {}

for l, n in locc.items(): # letter, number
    if n not in rlocc:
        rlocc[n] = [l]
    else:
        rlocc[n].append(l)

for n, l in reversed(sorted(rlocc.items())):
    print(l, n)
