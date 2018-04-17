from p89 import from_roman, to_roman, values

def compute_expectation(prefix='', prob=1.0):
  estimate = prob * from_roman(prefix)
  if prefix and estimate < 1e-15: return estimate
  candidates = []
  for letter in values.keys():
    candidate = prefix + letter
    if candidate == to_roman(from_roman(candidate)):
      candidates.append(candidate)
  if candidates:
    norm_factor = prob / (0.14 * len(candidates) + 0.02)
    cand_prob, term_prob = 0.14 * norm_factor, 0.02 * norm_factor
    expectations = [compute_expectation(c, cand_prob) for c in candidates]
    return sum(expectations) + term_prob * from_roman(prefix)
  else:
    return estimate

if __name__ == "__main__":
  print(compute_expectation())