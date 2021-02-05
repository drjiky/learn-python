#x et y 2 entiers donnes par ut si x>0 :si y<5 print x eet positf y<5
#si y>=5 print x est positif et y >=5
#si x=0: si y<5 print x est nul et y <5 si y>5 print x est nul et y>5
#si x<0:si y<5 printx est negatif et y<5
#x<0 y>=5 print x negatif et y>=5
x=int(input("enter x"))
y=int(input("enter y"))
if x>0 :
    if y<5:
        print("x est positif  et y<5")
    else:
        print("x est positif et y>=5")
elif x==0:
    if y<5:
        print("x est egal a zero et y<5")
    elif y>5:
        print("x est egale a zero et y >5")
else:
    if y<5:
        print("x est negatif et y <5")
    else:
        print("x est negatif et y>=5")    