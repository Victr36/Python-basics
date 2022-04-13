list_of_cubes = []
all_sum = 0
for i in range(1, 1001, 2):
    list_of_cubes.append(i ** 3)
for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]
    list_of_cubes[ind] += 17
print(all_sum)
