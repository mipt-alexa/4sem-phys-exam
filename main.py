from PIL import Image
import matplotlib.pyplot as plt


def moving_average(n, *array):
    return_arr = [array[0]]
    for j in range(1, len(array) - 1):
        sum_3 = sum(array[j - int(n / 2):j + int(n / 2)])
        return_arr.append(sum_3 / n)
    return_arr.append(array[len(array) - 1])
    return return_arr


def remove_noise(level, *array):
    return_arr = []
    for j in array:
        if j < level:
            return_arr.append(0)
        else:
            return_arr.append(j - level)
    return return_arr


image_id = input()

im = Image.open('image' + str(image_id) + '.jpg')
pix = im.load()

W = im.size[0]
H = im.size[1]

Lambda = []
for i in range(H):
    Lambda.append(i)

Data = []
R, G, B = [], [], []
for i in range(H):
    Data.append(pix[W / 2, i])
    R.append(pix[W / 2, i][0])
    G.append(pix[W / 2, i][1])
    B.append(pix[W / 2, i][2])

Int_1 = []
for i in Data:
    # Int_1.append(0.2126 * i[0] + 0.7152 * i[1] + 0.0722 * i[2])
    Int_1.append(0.299 * i[0] + 0.587 * i[1] + 0.114 * i[2])


num_average = 21

Int_1_mov_av = moving_average(num_average, *Int_1)
R_mov_av = moving_average(num_average, *R)
G_mov_av = moving_average(num_average, *G)
B_mov_av = moving_average(num_average, *B)


noise_lvl = 20
Int_1_noise = remove_noise(noise_lvl, *Int_1_mov_av)
R_noise = remove_noise(noise_lvl, *R_mov_av)
G_noise = remove_noise(noise_lvl, *G_mov_av)
B_noise = remove_noise(noise_lvl, *B_mov_av)

# print(Data)
# print(Int_1)

f, ((ax1, b1, c1), (ax2, b2, c2)) = plt.subplots(2, 3)

ax2.plot(Lambda, Int_1)
ax1.plot(Lambda, R, color="red")
ax1.plot(Lambda, G, color="green")
ax1.plot(Lambda, B, color="blue")

b2.plot(Lambda, Int_1_mov_av, label="скользящее среднее с n=" + str(num_average))
b1.plot(Lambda, R_mov_av, color="red")
b1.plot(Lambda, G_mov_av, color="green")
b1.plot(Lambda, B_mov_av, color="blue")


c1.plot(Lambda, R_noise, color="red")
c1.plot(Lambda, G_noise, color="green")
c1.plot(Lambda, B_noise, color="blue")
c2.plot(Lambda, Int_1_noise)

plt.legend()
plt.show()
