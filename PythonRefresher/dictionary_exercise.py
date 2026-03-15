my_vehicle = {
    "model":'BMW',
    "make":"Carbon",
    "year":2025,
    "mileage":20
}
for i in my_vehicle.items():
    print(i)

my_vehicle_2 = my_vehicle.copy()

print(my_vehicle_2)

my_vehicle_2["no_of_tires"] = 4

print(my_vehicle_2)

my_vehicle_2.pop("mileage")

print(my_vehicle_2)