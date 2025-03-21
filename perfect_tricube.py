import time

# user-defined integer
input_num = 2000000

start_time = time.time()

# pre-compute all the cubes to prevent repetitiveness later
all_cubes = []
n = 1
while True:
    n_cube = n ** 3
    if n_cube < input_num:
        all_cubes.append(n_cube)
        n += 1
    else:
        break

# maximum possible cube root to be considered
max_cube_root = len(all_cubes)

all_tricubes = []
# consider all the possible combinations of cube roots
for i in range(1, max_cube_root):  # the root of the first cubelet ranges from 1 to max_cube_root, but not being max_cube_root exactly
    i_cube = all_cubes[i-1]
    for j in range(i, max_cube_root):  # the root of the second cubelet starts from i
        j_cube = all_cubes[j-1]
        for k in range(j, max_cube_root):  # the root of the third cubelet starts from j
            k_cube = all_cubes[k-1]
            for n in range(k+1, max_cube_root+1):  # the root of the tri-cube is at least k+1, and could be up to max_cube_root
                n_cube = all_cubes[n-1]
                if i_cube + j_cube + k_cube == n_cube:
                    all_tricubes.append((n, n_cube, i, j, k))

# print out all the tricubes
print(len(all_tricubes), 'tricubes are found')
print('-'*20)
for tricube in all_tricubes:
    print(*tricube, sep=',')

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
