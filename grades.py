# grades.py
# Ask for a score or mark (out of a 100), and print out grade

score_str = input("What is your score, 0 to 100: ")
score = int(score_str)

print("Your grade is ", end="")

if score < 0 or score > 100:
    print("not valid!")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
else:
    print("F")
