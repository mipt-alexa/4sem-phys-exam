import matplotlib.pyplot as plt


for i in range(10):
    f = open("normalized_data/" + str(i) + ".txt")

    L, I, R, G, B = (zip(*[map(float, line.strip().split()) for line in f.readlines()]))

    plt.plot(L, I, label=str(i))


f = open("ocean_data.txt")
X, Y = zip(*[map(float, line.strip().split()) for line in f.readlines()])

plt.plot(X, Y, linestyle='--')

plt.legend()
plt.show()

# plt.show()
# plt.savefig("together")

