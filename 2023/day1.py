
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
            "zero": 0,
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


with open("day1.txt", "r") as file:
    for line in file:
        digits = re.findall(r"\d+|zero|one|two|three|four|five|six|seven|eight|nine", line)
        a = digits[0]
        b = digits[-1]
        out = ""
        if a.isdigit():
            out += str(a[0])
        else:
            out += str(number_mapping[a])
        if b.isdigit():
            out += str(b[-1])
        else:
            out += str(number_mapping[b])
        calibration_values.append(int(out))
        print(line, out)

sum_of_values = sum(calibration_values)
print(sum_of_values)
