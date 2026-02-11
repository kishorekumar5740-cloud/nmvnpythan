print("enter five marks:")
m1 = int(input("enter the m1: "))
m2 = int(input("enter the m2: "))
m3 = int(input("enter the m3: "))
m4 = int(input("enter the m4: "))
m5 = int(input("enter the m5: "))

tot = m1 + m2 + m3 + m4 + m5
avg = tot / 5

# Check if passed
if m1 > 34 and m2 > 34 and m3 > 34 and m4 > 34 and m5 > 34:
    res = "pass"
else:
    res = "fail"

# Calculate Grade
if res == "pass":
    if avg >= 85:
        gra = "outstanding"
    elif avg >= 75:
        gra = "excellent"
    elif avg >= 65:
        gra = "very good"
    elif avg >= 55:
        gra = "good"
    else:
        gra = "fair"
else:  # This else belongs to 'if res == "pass"'
    gra = "no grade because fail"

print("total mark:", tot)
print("average mark:", avg)
print("result :", res)
print("grade:", gra)
