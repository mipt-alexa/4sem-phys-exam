from PIL import Image
import matplotlib.pyplot as plt

def moving_average(n, *array):
    return_arr = []
    for j in range(1, len(array) - 1):
        sum_3 = sum(array[j - int(n / 2):j + int(n / 2)])
        return_arr.append(sum_3 / n)
    return_arr.insert(0, return_arr[0])
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


for image_id in range(9):

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

    noise_lvl = int( sum(Int_1_mov_av[0: 0.2 * H]) / 0.2 / H )
    Int_1_noise = remove_noise(noise_lvl, *Int_1_mov_av)
    R_noise = remove_noise(noise_lvl, *R_mov_av)
    G_noise = remove_noise(noise_lvl, *G_mov_av)
    B_noise = remove_noise(noise_lvl, *B_mov_av)

    file2 = open('data/' + str(image_id) + '.txt', 'w')

    for i in range(len(Int_1_noise)):
        file2.write(str(Int_1_noise[i]) + " " + str(R_noise[i]) + " " + str(G_noise[i]) + ' ' + str(B_noise[i]) + '\n')
