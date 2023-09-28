# Submitted by: Carbonel, Radge Daryll A.
# BSCS - 1
# CC2 - 1B
# September 6, 2023

lbs = 320
kg = lbs/2.205
kg = round(kg,2)
lbs = str(lbs)
kg = str(kg)

mi = 22.3
km = mi*1.609
km = round(km,2)
mi = str(mi)
km = str(km)

fahrenheit = 9999
celsius = (5/9)*(fahrenheit-32)
celsius = round(celsius,2)
fahrenheit = str(fahrenheit)
celsius = str(celsius)

studentAge = [23, 20, 21, 21, 19, 22, 24, 26, 20, 22]
studentAge = sum(studentAge)
average = (studentAge)/10
studentAge = ["23", "20", "21", "21", "19", "22", "24", "26", "20", "22"]
average = str(average)

names = ["Albert Van Gogh", "Trixie Mentia", "Ethan Lee", "Szean Tao", "Zhao Lee"]
kingdomNames = ["Arkdenm", "Manyger"]
equipmentNames = ["Demonheart Sword", "Floyen Armor"]
abilities = ["Boost", "Enhance"]

print("Weight in Pounds (lbs): " + lbs)
print("Weight converted to kilograms (kg): " + kg)
print("=================================")
print("Length in Miles (mi): " + mi)
print("Length converted to Kilometers: " + km)
print("=================================")
print("Temperature in Fahrenheit (°f): "+ fahrenheit)
print("Temperature converted to Celsius (°C): "+ celsius)
print("=================================")
print("Age of Student 1: " + studentAge[0])
print("Age of Student 2: " + studentAge[1])
print("Age of Student 3: " + studentAge[2])
print("Age of Student 4: " + studentAge[3])
print("Age of Student 5: " + studentAge[4])
print("Age of Student 6: " + studentAge[5])
print("Age of Student 7: " + studentAge[6])
print("Age of Student 8: " + studentAge[7])
print("Age of Student 9: " + studentAge[8])
print("Age of Student 10: " + studentAge[9])
print("The average age of the students is: " + average)
print("=================================")
print(f"""A student named {names[0]} and his friend named {names[3]} were walking to school. When they were
crossing a pedestrian lane, a truck at full speed came and killed {names[0]} and {names[3]}. After a while, 
they woke up surrounded by twin knights named {names[2]} and {names[4]}. They were transported to the kingdom 
of {kingdomNames[0]}. A few days later, they were given {equipmentNames[0]} and {equipmentNames[1]} and they also 
found out that the twin knights, {names[2]} and {names[4]}, were the first knights of Duke Floyen. The twin knights
taught {names[0]} and {names[3]} abilities like {abilities[0]} and {abilities[1]}, which can be used in combat.
After months of training, {names[0]} and {names[3]} wanted to go to another kingdom named, {kingdomNames[1]}, where 
{names[1]} was the ruler of the kingdom. They went and said their farewells to {names[2]} and {names[4]}. They started 
their travels to go to the kingdom of {kingdomNames[1]}, where they may encounter many problems and hindraces along the way.""")
