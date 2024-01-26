guests = {input() for _ in range(int(input()))}

command = input()
while command != "END":
    code = command
    if code in guests:
        guests.remove(code)

    command = input()

print(len(guests))
print(*(sorted(guests)), sep="\n")
