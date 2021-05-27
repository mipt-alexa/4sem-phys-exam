import matplotlib.pyplot as plt


for i in range(3):
    f = open("normalized_data/" + str(i) + ".txt")

    L, I, R, G, B = (zip(*[map(float, line.strip().split()) for line in f.readlines()]))

    plt.plot(L, I)


# plt.show()
plt.savefig("together")

