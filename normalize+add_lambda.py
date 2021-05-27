MAX_LAMBDA = 845
DELTA_LAMBDA = 25


def find_half_width(max_val, *arr):
    max_val /= 2
    a, b = 0, 0
    for j in range(len(arr)):
        if arr[j - 1] < max_val <= arr[j]:
            a = arr.index(arr[j])
        if arr[j - 1] >= max_val > arr[j]:
            b = arr.index(arr[j])
    return [a, b]


for i in range(3):
    f = open("data/" + str(i) + ".txt")

    I, R, G, B = zip(*[map(float, line.strip().split()) for line in f.readlines()])

    max_value = max(I)
    max_index = I.index(max_value)
    print(max_index)

    print(find_half_width(max_value, *I))
