print("LAND PARCEL AREA AND PERIMETER CALCULATOR")
number_of_points = int(input("Enter the number of boundary points: "))
print("you entered", number_of_points, "points.")
coordinates = []
for i in range(number_of_points):
    print("Point", i+1)
    easting = float(input("Enter Easting (m): "))
    northing = float(input("Enter northing (m): "))
    coordinates.append((easting, northing))
print("Coordinates entered:")
print(coordinates)
area = 0
n = len(coordinates)
for i in range(n):
     x1, y1 = coordinates[i]
     x2, y2 = coordinates[(i+1) % n]
     area = area + (x1 * y2 - y1 * x2)
area = abs(area) / 2
print("Area =", area, "m2")
hectares = area / 10000
acres = area / 4046.856
print("Area in heactares =", hectares, "ha")
print("Area in acres =", acres, "acres")
import math
perimeter = 0
for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i+1) % n]
        distance = math.sqrt((x2 - x1) **2 + (y2 -y1) **2 )
        perimeter = perimeter + distance
print("Perimeter =", perimeter, "m")
# Save results to a text file
with open("land_parcel_results.txt", "w") as file:
    file.write("LAND PARCEL CALCULATOR RESULTS\n")
    file.write(f"coordinates: {coordinates}\n")
    file.write(f"Area in hectares: {hectares} ha\n")
    file.write(f"Area in acres: {acres} acres\n")
    file.write(f"perimeter: {perimeter} m\n")
print("Results saved successfully!")
