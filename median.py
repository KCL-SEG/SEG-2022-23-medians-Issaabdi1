"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) % 2 == 1:
    position = (len(numbers) - 1) / 2
    median = numbers[int(position)]
    print(median)
else:
    pos = (len(numbers) / 2) - 1
    value1 = numbers[int(pos)]
    value2 = numbers[int(pos + 1)]
    median = (value1 + value2) / 2
    print(median)
