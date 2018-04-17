values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
keys = {v: k for k, v in values.items()}
ordered_values = sorted(keys.keys(), reverse=True)
subtract_values = [100, 100, 10, 10, 1, 1, 0]

def from_roman(s):
  total = 0
  for i, c in enumerate(s):
    value = values[c]
    if i < len(s) - 1 and values[s[i+1]] > value:
      value = -value
    total += value
  return total

def to_roman(v):
  s = ''
  idx = 0
  while v > 0:
    value = ordered_values[idx]
    if v >= value:  # whole values
      s += keys[value]
      v -= value
    elif v >= value - subtract_values[idx]:  # 4 or 9
      sub = subtract_values[idx]
      s += keys[sub] + keys[value]
      v -= value - sub
      idx += 1
    else:
      idx += 1
  return s

if __name__ == "__main__":
  with open('data/p089_roman.txt', 'r') as f:
    total_saved = 0
    for line in f:
      line = line.strip()
      roman = to_roman(from_roman(line))
      saving = len(line) - len(roman)
      if saving > 0:
        total_saved += saving
      elif saving < 0:
        print("Error: new form %s is longer than original %s." % (roman, line))
    print(total_saved)