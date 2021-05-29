MAX_LAMBDA = 843
DELTA_LAMBDA = 31


def find_half_width(max_val, *arr):
    max_val /= 2
    a, b = 0, 0
    for j in range(len(arr)):
        if arr[j - 1] < max_val <= arr[j]:
            a = arr.index(arr[j])
        if arr[j - 1] >= max_val > arr[j]:
            b = arr.index(arr[j])
    return [a, b]


for i in range(9):
    f = open("data/" + str(i) + ".txt")

    I, R, G, B = zip(*[map(float, line.strip().split()) for line in f.readlines()])

    max_value = max(I)
    max_index = I.index(max_value)
    print(max_index)

    [i1, i2] = find_half_width(max_value, *I)
    nm_per_pixel = 2 * DELTA_LAMBDA / (i2 - i1)

    file2 = open('normalized_data/' + str(i) + '.txt', 'w')

    _lambda = 0

    for k in range(len(I)):
        _lambda = 870 + (k - i2) * nm_per_pixel
        file2.write(str(_lambda) + " " + str(I[k] / max_value) + " " + str(R[k]/255) + " " + str(G[k]/255) +
        ' ' + str(B[k]/255) + '\n')
        # file2.write(str(_lambda) + " " + str(I[k]) + " " + str(R[k]) + " " + str(G[k]) + " " + str(B[k]) + '\n')
