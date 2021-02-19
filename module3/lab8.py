blocks = int(input("Enter the number of blocks: "))
layer=1
height=0
while blocks>=layer:
    blocks=blocks-layer
    layer+=1
    height+=1

#
# Write your code here.
#	

print("The height of the pyramid:", height)
