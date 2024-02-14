from pyfiglet import figlet_format


input_message = input()
message_as_ascii_art = figlet_format(input_message, font='slant')
print(message_as_ascii_art)