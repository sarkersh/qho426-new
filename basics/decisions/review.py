# Activity 3: Review
#vowel a,e,i,o,u
ch = input()
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")


num1 = 190
num2 = 110
num3 = 180
if ((num1 > num2) and (num1 > num3)):
    print(num1)
elif ((num2 > num1) and (num2 > num3)):
    print(num2)
else:
    print(num3)