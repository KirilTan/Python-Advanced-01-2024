from collections import deque

green_light_duration = int(input())  # Duration of green light in seconds
free_window_duration = int(input())  # Duration of free window in seconds

cars_in_line = deque()
cars_passed = 0

while True:
    command = input()

    if command == "END":
        break

    if command == "green":
        current_green_light_duration = green_light_duration

        while cars_in_line and current_green_light_duration > 0:
            current_car = cars_in_line.popleft()
            car_length = len(current_car)

            if current_green_light_duration >= car_length:
                # The car passes completely during the green light
                cars_passed += 1
                current_green_light_duration -= car_length
            else:
                # Car partially passes, and we need to check the free window
                car_length -= current_green_light_duration
                if car_length <= free_window_duration:
                    # The car passes safely during the free window
                    cars_passed += 1
                else:
                    # A crash happens
                    crash_index = current_green_light_duration + free_window_duration
                    crash_char = current_car[crash_index] if crash_index < len(current_car) else current_car[-1]
                    print(f"A crash happened!")
                    print(f"{current_car} was hit at {crash_char}.")
                    exit()  # End the script after a crash
                break  # Exit the loop after processing the car in the free window

    else:
        cars_in_line.append(command)

# If the loop ends normally, print the safe message
print(f"Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")
