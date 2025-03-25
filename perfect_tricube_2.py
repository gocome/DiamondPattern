import time

# user-defined integer
input_num = 2000000

start_time = time.time()

# pre-compute all the cubes to prevent repetitiveness later, using a set instead of a list
all_cubes = {}  # use a dictionary instead of a list
n = 1
while True:
    n_cube = n ** 3
    if n_cube < input_num:
        all_cubes[n_cube] = n  # Use .add() to insert into a set
        n += 1
    else:
        break

# maximum possible cube root to be considered
max_cube_root = n  # max_cube_root should be the value of n, not the length of all_cubes

all_tricubes = []
# consider all the possible combinations of cube roots
for i in range(1, max_cube_root):  # the root of the first cubelet ranges from 1 to max_cube_root, but not being max_cube_root exactly
    i_cube = i ** 3
    for j in range(i, max_cube_root):  # the root of the second cubelet starts from i
        j_cube = j ** 3
        for k in range(j, max_cube_root):  # the root of the third cubelet starts from j
            k_cube = k ** 3
            ijk_cube_total = i_cube + j_cube + k_cube
            # Check if the sum of the cubes is in the set
            if ijk_cube_total in all_cubes.keys():  # the dictionary keys is a set
                all_tricubes.append((all_cubes[ijk_cube_total], ijk_cube_total, i, j, k))

# print out all the tricubes
print(len(all_tricubes), 'tricubes are found')
print('-'*20)
for tricube in all_tricubes:
    print(*tricube, sep=',')

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")