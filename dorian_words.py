file = open("dorian.txt", 'r')
# 1) count occurrences for all words in the text
wocc, wlen = {}, {}  # words occurrences and lengths
for line in file:
    words = line.strip().lower().split()
    for w in words:
        w = w.strip(".,;:-'`\"?!()")
        if not (w in wocc):
            wocc[w] = 1
            wlen[w] = len(w)
        else:
            wocc[w] += 1
file.close()
# 2) reverse the dictionaries
rwocc = {}
rwlen = {}
for w, z in wocc.items():
    if z not in rwocc:
        rwocc[z] = [w]
    else:
        rwocc[z].append(w)
for w, z in wlen.items():
    if z not in rwlen:
        rwlen[z] = [w]
    else:
        rwlen[z].append(w)
# 3) print the results
top8length = sorted(rwlen.items())
top20words = sorted(rwocc.items())
print(top8length[-8:])
print(top20words[-20:])
