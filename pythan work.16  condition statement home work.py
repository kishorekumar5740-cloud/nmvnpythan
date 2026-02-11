#greatest among 3 numbers

#num1=int(input("enter the num1 :"))
#num2=int(input("enter the num2 :"))
#num3=int(input("enter the num3 :"))
#num=max(num1,num2,num3)
#print("greatest number is :",num)


#given no is positive or negative or zero
#num=float(input("enter the number :"))
#if num>0:
#    print("positive value")
#elif num<0:
#    print("negative value")
#else :
#    print(" zero value")

#age eligible to marriage
gender=(input("enter the gender :"))
age=int(input("enter the  age :"))
if gender == "male":
    if age >= 23:
        print("Eligible for marriage")
    else:
        print("Not eligible")
        
elif gender == "female":
    if age >= 21:
        print("Eligible for marriage")
    else:
        print("Not eligible")
        
else:
    print("Invalid gender ")


