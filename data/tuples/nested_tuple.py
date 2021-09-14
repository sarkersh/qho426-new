"""Activity 3: Nested Tuples

List and tuples are data structures that can be nested.  This means that we can place lists inside lists,
tuples inside tuples or we can nest one inside the other i.e. tuples inside a list or lists inside tuples.

# Returns a list of teachers with tuples
def list_of_teachers():
  return [ ("Prins", "Module Leader"),  ("Darren", "Tutor"), ("Nick", "Tutor") ]"""
def steps():
    all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return all_steps
def run():
    all_steps = steps()
    good_steps = []
    bad_steps = []
    for step in all_steps:
        if (step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()