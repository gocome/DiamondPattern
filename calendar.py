# A2.4 Calendar
# S.Chen
# Makes a calendar of a month with input of start day and length of month
# sources:

# 2 inputs, one for length and one for start day
inputnum = 0
inputstart = ()

# variable for amount of days until first day (the gap at the start)
# spacedays = 0

# which day does it start, while making sure it's a valid day
while not inputstart in ("N", "M", "T", "W", "R", "F", "S"):
    inputstart = input("What day does the month start on? ")

# length of 28 to 31, waits until valid number
while inputnum < 28 or inputnum > 31:
    inputnum = int(input("How many days in the month? "))

# # Setup header of weekdays
# S = False
# for e in ("S", "M", "T", "W", "Th", "F", "S"):
#     # make sure 1 space before first S and Th
#     if e == "S" and S == False or e == "Th":
#         # these will only get 1 space
#         print(" ", end="")
#         # wont run with saturday
#         S = True
#     else:
#         # rest get 2 spaces
#         print("  ", end="")
#     print(e, end="")
# print()
#
days = ["S", "M", "T", "W", "Th", "F", "S"]
format_string = ' '.join(['{:>2}']*7)  # repeat '{:>2}' by 7 times and then join together with a space in between,
                                        # resulting in format_string of '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'
days_string = format_string.format(*days)  # replace '{:>2}' by each day while keeping the width of 2 symbols
                                            # if the day is a single symbol, prepend a space to get 2 symbols
print(days_string)

# # Setup line of -
# for e in range(0, 20):
#     print("-", end="")
# print()
#
dash_string = ''.join(['-']*20)
print(dash_string)

num_list = []
# find the first day
for day in ("N", "M", "T", "W", "R", "F", "S"):
    # runs until the inputed start day is the same as the one in the list
    if day == inputstart:
        break
    # # the program will run twice for "M", so spacedays will = 2 for monday
    # spacedays += 1
    # # the actual spaces
    # print("   ", end="")
    num_list.append('')

# range is 1 to inputnum + 1 so print(day) doesn't give 0 on first day
for day in range(1, inputnum + 1):
    # # checks if a new line must be made
    # # (if spacedays and days added together is divisible by a week or 7 plus one because no extra spaces)
    # # this if statement runs on the first day so that is makes sure its not the first day
    # # it's supposed to run on the 8th, 15th, 22nd, etc TOTAL days
    # if (day + spacedays) % 7 == 1 and day != 1:
    #     print()
    # # extra space if not
    # else:
    #     print(" ", end="")
    # # extra space if one digit number and not 1st day
    # if day > 1 and day < 10:
    #     print(" ", end="")
    # # finally print the day
    # print(day, end="")
    num_list.append(day)
    if len(num_list) == 7:
        num_string = format_string.format(*num_list)
        print(num_string)
        num_list = []

if num_list:
    format_string = ' '.join(['{:>2}']*len(num_list))
    num_string = format_string.format(*num_list)
    print(num_string)
