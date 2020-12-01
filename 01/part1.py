file = open('input', 'r')

numbers = []

for line in file:
  numbers.append(int(line))

for num in numbers:
  other = 2020 - num
  if other in numbers:
    print(f"{other * num}")
    exit()

