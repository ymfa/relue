total = 0
for number in [3, 5]:
  n = number
  while n < 1000:
    if number != 5 or n % 15 != 0:
      total += n
    n += number

print(total)