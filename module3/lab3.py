year=int(input())
if year%4 !=0:
    print("it's a commun year")
elif year%100!=0:
    print("it's a leap year")
elif year%400!=0:
    print("it's a commun year") 
else:
    print("it's a leap year")           