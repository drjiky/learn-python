#converting decimal to binary
#etant donne n un entier positif,ecrire la chaine binaire de n
#n=5,n%2=1,n//2=2,
n=int(input())
while n>0 :
    print(n%2)
    n=n//2
    
   