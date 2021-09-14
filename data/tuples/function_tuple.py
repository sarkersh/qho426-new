"""Activity 2: Tuple Return Type
One feature of tuples and functions is that a function can return a tuple (same also applies to lists).
This can be very useful when we wish to return more than one value from a function and have an immutable data type."""
# Returns a tuple with names of teachers:
def teachers():
  return ("Prins", "Darren", "Nick")

def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run():
  probabilities = likelihood()
  print(f"Minimum likelihood of falling: {probabilities[0]}%")
  print(f"Maximum likelihood of falling: {probabilities[1]}%")

run()