wedding = {"items":{"Cake":1, "Car":1, "Ribbons":100},"people":{"guests":30}}
for key, value in wedding.items():
    print(f"{key}: {value}")
def short_pattern():
    pattern = {"sequence":"101","occurrences":5}
    return pattern
def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern
def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern
def run():
    print("Analysing patterns...")
    patterns = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern()
    }
    for key, value in patterns.items():
        print(f"{key}: {value}")

run()
