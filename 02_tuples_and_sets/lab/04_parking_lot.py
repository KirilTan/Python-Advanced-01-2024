number_of_inputs = int(input())

parking_lot = set()

for _ in range(number_of_inputs):

    direction, plate = input().split(", ")

    if direction == "IN":
        parking_lot.add(plate)
    elif direction == "OUT":
        if parking_lot:
            parking_lot.remove(plate)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print(f"Parking Lot is Empty")
