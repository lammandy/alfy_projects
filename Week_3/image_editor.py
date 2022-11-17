image = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
new_list = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]]

def divide_channels(image):
    result = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(image[0][0])):
                pass
    for x in image:
        for y in x:
            for z in y:
                result.append([[z]])
            # for z in y:
            #     [list(z)]
                # for i in range(len(y)):
                    # n_lst.append(z)
                    # new_list[x][y][i] = z
                    # print(new_list[x][y][i])
    return result

# new = divide_channels(image)
# print(new)
# print(new_list)
image_1 = [[[1, 2]]]
print(divide_channels(image_1))