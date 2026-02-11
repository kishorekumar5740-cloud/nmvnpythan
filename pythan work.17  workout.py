 #voter
#age=int(input("enter your age :"))
#if age>=18:
#    print("eligible to vote")
#else:
#    print("not eligible to vote")

#even or odd
#num=int(input("enter your number:"))
#if num%2==0 :
#    print("even number")
#else:
#    print("odd number")

#leap year or not
#num=int(input("enter your number :"))
#if(num%400==0):
#        print("leap year")
#else:
 #       print("not leap year")
        
#greatest among
#num1= float(input(" enter the num 1:"))
#num2= float(input(" enter the num 2:"))
#if num1>num2:
#        print(num1," is greater")
#else:
#    print(num2," is greater")
    
#palindrone
#name=input("enter your string :")
#rname= name[::-1]
#print("reverse name :",rname)
#if name==rname:
#    print("palindrone")
#else:
#    print("not palindrone")

#mark statement
#avg=int(input("enter the avg :"))
#if avg >=85:
	#print("outstanding")

#elif avg>=75:
#	print("excellent")
#elif avg>=65:
#	print("ver good")
#elif avg>=55:
#	print("good")
#elif avg>=45:
#	print("fair")
#else:
#	print("low average")

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

print("-------------------")
print("total mark:", tot)
print("average mark:", avg)
print("result :", res)
print("grade:", gra)



    



    
