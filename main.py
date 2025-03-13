# input
lines = int(input("How many lines? "))

# calculate how many lines in the upper triangle of the diamond
half_lines = (lines + 1) // 2

# calculate locations of two hashtags in the first line
# if p == q, there is only one hashtag because two hashtags appear in the same place
p = q = (lines - 1) // 2

# store the hashtag locations of every line in the list 'hashtags'
hashtags = []

# calculate the hashtag locations from the lines in the upper triangle
for _ in range(half_lines):
    hashtags.append([p, q])
    p -= 1
    q += 1

# calculate the hashtag locations from the lines in the lower triangle
# note that the lower triangle is the reflective upper triangle
for i in range(half_lines, lines):
    j = lines - i - 1
    hashtags.append(hashtags[j])

# print out the diamond once the hashtag locations are all ready
# (separating the data calculation from IO operations is highly preferred)
for hashtag in hashtags:
    for i in range(hashtag[1]):
        if i == hashtag[0]:
            print('#', end='')
        else:
            print(' ', end='')
    print('#')

