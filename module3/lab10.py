numbers=[5,10,41,82,7,1,21,8,12,13]
pair=[]
impair=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        pair.append(numbers[i])
    else:
        impair.append(numbers[i])
print(pair)
print(impair)
   