# Key input
number_in_base_10 = -1
base = 0

while number_in_base_10 < 0:
    number_in_base_10 = int(input("What base ten number?"))
    if number_in_base_10 < 0:
        print("The number must be positive.")

while base < 2 or base > 9:
    base = int(input("What base?"))
    if base < 2 or base > 9:
        print("The base must be between 2 and 9.")

# Compute digits
# Here we find the last digit first, and then the last second digit, until the first digit.
digit_list = []
quotient = number_in_base_10
if quotient == 0:
    digit_list.append(0)
else:
    while quotient > 0:
        quotient, remainder = quotient // base, quotient % base
        digit_list.append(remainder)

# Print output
digit_list = reversed(digit_list)
print(number_in_base_10, " in base ", base, " is ", *digit_list, ".", sep="")
