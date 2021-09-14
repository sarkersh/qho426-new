print("How many bars should be charged?")
bars_to_charged = int(input())
bars_charged = 0
print()
while(bars_charged < bars_to_charged):
    print("Charging:", end="")
    bars_charged = bars_charged + 1
    print(" █" * bars_charged)
print("The battery is fully charged.")