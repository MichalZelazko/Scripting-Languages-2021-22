import pickle
import time


datafile = open("substr_1e3.pkl", 'rb')
data = pickle.load(datafile)
datafile.close()
n = len(data)
maxsum = 0
start = time.time()
for p in range(0, n):
    for q in range(p, n):
        s = 0
        for i in range(p, q+1):
            s += data[i]
        maxsum = max(maxsum, s)
t = time.time()-start
print(f"Elements: {n}\t Max sum: {maxsum}")
print(f"Execution time: {t}")


datafile = open("substr_1e3.pkl", 'rb')
data1 = pickle.load(datafile)
datafile.close()
n = len(data1)
maxsum1 = 0
start1 = time.time()
for p in range(0, n):
    for q in range(p, n):
        maxsum1 = max(maxsum1, sum(data1[p:q+1]))
t1 = time.time()-start1
print(f"\nElements: {n}\t Max sum: {maxsum1}")
print(f"Execution time: {t1}")


datafile = open("substr_1e3.pkl", 'rb')
data2 = pickle.load(datafile)
datafile.close()
n = len(data2)
max_so_far = data2[0]
max_ending_here = 0
start2 = time.time()
for p in range(0, n):
    max_ending_here = max_ending_here + data2[p]
    if (max_so_far < max_ending_here):
        max_so_far = max_ending_here
    elif max_ending_here < 0:
        max_ending_here = 0

t2 = time.time()-start2
print(f"\nElements: {n}\t Max sum: {max_so_far}")
print(f"Execution time: {t2}")
