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


image_id = 6

im = Image.open('sourse_images/image' + str(image_id) + '.jpg')
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

num_average = int(0.05 * H)

Int_1_mov_av = moving_average(num_average, *Int_1)
R_mov_av = moving_average(num_average, *R)
G_mov_av = moving_average(num_average, *G)
B_mov_av = moving_average(num_average, *B)

noise_lvl = int(sum(Int_1_mov_av[0: int(0.2 * H)]) / 0.2 / H)
Int_1_noise = remove_noise(noise_lvl, *Int_1_mov_av)
R_noise = remove_noise(noise_lvl, *R_mov_av)
G_noise = remove_noise(noise_lvl, *G_mov_av)
B_noise = remove_noise(noise_lvl, *B_mov_av)

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

ax2.set_xlabel("pixel coordinate")
b2.set_xlabel("pixel coordinate")
c2.set_xlabel("pixel coordinate")

ax1.set_ylabel("RGB-levels")
ax2.set_ylabel("Intensity")
ax1.axes.get_xaxis().set_visible(False)
b1.axes.get_xaxis().set_visible(False)
c1.axes.get_xaxis().set_visible(False)

b1.axes.get_yaxis().set_visible(False)
c1.axes.get_yaxis().set_visible(False)
b2.axes.get_yaxis().set_visible(False)
c2.axes.get_yaxis().set_visible(False)

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.95,
                    top=0.95,
                    wspace=0.12,
                    hspace=0.15)

plt.show()
