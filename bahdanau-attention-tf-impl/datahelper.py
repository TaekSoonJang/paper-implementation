import random
import string

def get_random_chars(num_units, length=10):
  X = []
  y = []
  for i in range(num_units):
    data = ''.join([random.choice(string.ascii_letters) for n in range(length)]).lower()
    X.append(data)
    y.append(''.join(sorted(data)))

  return X, y