#prompt user to enter a number list
#write a code that eats even numbers
liste=input("enter a number")
for number in liste :

    if int(number)%2==0: 
        continue
    print(number,end="")    
