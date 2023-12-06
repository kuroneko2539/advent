
import re
import re

calibration_values = []

with open("day1.txt", "r") as file:
    for line in file:
        first_digit = re.search(r"\d", line).group()
        last_digit = re.findall(r"\d", line)[-1]
        calibration_values.append(int(first_digit + last_digit))

sum_of_values = sum(calibration_values)
print(sum_of_values)


calibration_values = []
number_mapping = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

def process_line(line):
    digits = re.findall(r"\d+|one|two|three|four|five|six|seven|eight|nine", line)
    if len(digits) < 1:
        return None
    elif len(digits) < 2:
        if len(digits[0]) > 1:
            return int(str(digits[0][0]) + str(digits[0][-1]))
        else:
            return None

    first_digit = digits[0]
    last_digit = digits[-1]

    if first_digit.isdigit():
        first_digit = first_digit[0]
    else:
        first_digit = number_mapping[first_digit]

    if last_digit.isdigit():
        last_digit = last_digit[-1]
    else:
        last_digit = number_mapping[last_digit]

    return int(str(first_digit) + str(last_digit))


with open("day1.txt", "r") as file:
    for line in file:
        out = process_line(line)
        if out:
            calibration_values.append(int(out))
        print(line, out)

sum_of_values = sum(calibration_values)
print(sum_of_values)
