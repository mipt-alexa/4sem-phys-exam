import matplotlib.pyplot as plt

NUMBER_IMAGES = 10

L = [[] for i in range(NUMBER_IMAGES)]
I = [[] for i in range(NUMBER_IMAGES)]
R = [[] for i in range(NUMBER_IMAGES)]
G = [[] for i in range(NUMBER_IMAGES)]
B = [[] for i in range(NUMBER_IMAGES)]

for i in range(NUMBER_IMAGES):
    f = open("normalized_data/" + str(i) + ".txt")

    L[i], I[i], R[i], G[i], B[i] = (zip(*[map(float, line.strip().split()) for line in f.readlines()]))

    # plt.plot(L, I)


L_a = []
I_a = []
R_a = []
G_a = []
B_a = []

indexes = [0 for i in range(NUMBER_IMAGES)]
print(indexes)

START_L = 730
END_L = 950

for k in range(NUMBER_IMAGES):
    while L[k][indexes[k]] < START_L:
        indexes[k] += 1


sum1 = 0
counter = 0
for j in range(START_L, END_L, 1):
    L_a.append(j)
    sum1 = 0
    counter = 0
    for k in range(1, NUMBER_IMAGES):
        while L[k][indexes[k]] < j:
            sum1 += I[k][indexes[k]]
            counter += 1
            indexes[k] +=1
    if counter == 0:
        I_a.append(0)
    else:
        I_a.append(sum1 / counter)

# red
indexes = [0 for i in range(NUMBER_IMAGES)]

for k in range(NUMBER_IMAGES):
    while L[k][indexes[k]] < START_L:
        indexes[k] += 1

for j in range(START_L, END_L, 1):
    sum1 = 0
    counter = 0
    for k in range(1, NUMBER_IMAGES):
        while L[k][indexes[k]] < j:
            sum1 += R[k][indexes[k]]
            counter += 1
            indexes[k] +=1
    if counter == 0:
        R_a.append(0)
    else:
        R_a.append(sum1 / counter)

# green
indexes = [0 for i in range(NUMBER_IMAGES)]

for k in range(NUMBER_IMAGES):
    while L[k][indexes[k]] < START_L:
        indexes[k] += 1

for j in range(START_L, END_L, 1):
    sum1 = 0
    counter = 0
    for k in range(1, 6):
        while L[k][indexes[k]] < j:
            sum1 += G[k][indexes[k]]
            counter += 1
            indexes[k] +=1
    if counter == 0:
        G_a.append(0)
    else:
        G_a.append(sum1 / counter)

# blue
indexes = [0 for i in range(NUMBER_IMAGES)]

for k in range(NUMBER_IMAGES):
    while L[k][indexes[k]] < START_L:
        indexes[k] += 1

for j in range(START_L, END_L, 1):
    sum1 = 0
    counter = 0
    for k in range(1, NUMBER_IMAGES):
        while L[k][indexes[k]] < j:
            sum1 += B[k][indexes[k]]
            counter += 1
            indexes[k] +=1
    if counter == 0:
        B_a.append(0)
    else:
        B_a.append(sum1 / counter)


plt.plot(L_a, I_a)
plt.plot(L_a, R_a, color="red")
plt.plot(L_a, G_a, color="green")
plt.plot(L_a, B_a, color="blue")


f = open("ocean_data.txt")
X, Y = zip(*[map(float, line.strip().split()) for line in f.readlines()])

plt.plot(X, Y, linestyle='--')

plt.show()

# plt.show()
# plt.savefig("together")

