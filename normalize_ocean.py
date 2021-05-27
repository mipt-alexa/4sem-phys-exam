f = open("ocean_data.txt")
L, I = zip(*[map(float, line.strip().split()) for line in f.readlines()])

max_val = max(I)

file2 = open("ocean_data.txt", 'w')

for k in range(len(I)):
     file2.write(str(L[k]) + ' ' + str(I[k] / max_val) + '\n')
