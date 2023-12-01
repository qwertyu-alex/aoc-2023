from sys import stdin, stdout

file = open('./1/in', 'r')
rows = file.readlines()

numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

two_digits = []


def find_first_number(row):
    for i, _ in enumerate(row):
        for number in numbers:
            if number in row[:i]:
                first = numbers[number]
                return first


def find_last_number(row):
    for i, _ in enumerate(row):
        for number in numbers:
            if number in row[len(row) - (i + 1):len(row)]:
                last = numbers[number]
                return last


for row in rows:
    first = ""
    last = ""

    first = find_first_number(row)
    last = find_last_number(row)

    two_digit = int(f"{first}{last}")
    two_digits.append(two_digit)

print(sum(two_digits))
