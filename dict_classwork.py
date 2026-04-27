car = {
    "brand" : "Tayota",
    "model" : "Camry",
    "rang" : "black",
    "narx" : 45_000,
    "type" : "sedan",
    "rang" : "blue"
}
# print(car)
car["model"]="Land Cruiser"
# print(car)
car["yil"] = 2025
print(car)
if "type" in car:
    print(True)
else:
    print(False)