''' Experiments with Hailstone sequences '''

def next_hsn(c):
    ''' Return next hsn-number'''
    if c % 2 == 0:
        return c//2
    else:
        return 3*c+1

def hsn(c):
    ''' Return full hsn-sequence for seed c'''
    sequence = [c]
    while c > 1:
        c = next_hsn(c)
        sequence.append(c)
    return sequence
'''
LIMIT = 100
longest = 0
longestElement = []
occurences = 0
highestValue = 0

for i in range(LIMIT+1):
    if longest < len(hsn(i)):
        longest = len(hsn(i))
for i in range(LIMIT+1):
    if len(hsn(i)) == longest:
        longestElement.append(i)
        occurences += 1

print(
    f"The length of the longest sequence is {longest}",
    f"The longest sequence appears for the element number {longestElement}",
    f"Such a sequence occurs {occurences} times",
    sep='\n'
    )


'''

LIMIT = 100
hsn_all = []
hsn_len = []
hsn_max = []
hsn_sum = []
for seed in range(0, LIMIT+1):
    s = hsn(seed)
    hsn_all.append(s)
    hsn_len.append(len(s))
    hsn_max.append(max(s))
    hsn_sum.append(sum(s))
print(hsn_all)
print(hsn_len)
print(hsn_max)
print(hsn_sum)
hsn_longest = max(hsn_len)
hsn_longest_seed = hsn_len.index(hsn_longest)
print(
    f"Problem 1, for range 0 to {LIMIT}",
    f"The longest sequence has {hsn_longest} elements",
    f"It occurs for element(s) {hsn_longest_seed}",
    sep='\n'
    )

