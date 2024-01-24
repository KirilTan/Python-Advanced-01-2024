clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_needed = 1
while clothes_in_box:
    current_clothing = clothes_in_box.pop()

    if current_rack_capacity >= current_clothing:
        current_rack_capacity -= current_clothing

    else:
        racks_needed += 1
        current_rack_capacity = rack_capacity - current_clothing

print(racks_needed) # 0.04
