import matplotlib.pyplot as plt
import numpy

f = open("ocean_data.txt")
X, Y = zip(*[map(float, line.strip().split()) for line in f.readlines()])

plt.plot(X, Y)

# plt.show()
plt.savefig("ocean")
