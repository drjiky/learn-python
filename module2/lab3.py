hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
totalmins=mins+dura
nbrhour=totalmins//60
nbrmins=totalmins%60
print(hour+nbrhour,":",nbrmins)