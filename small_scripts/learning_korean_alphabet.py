import random


def get_random_korean_letter():
    return random.choice(korean_letters_list)


korean_letters_list = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ',
                       'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅉ', 'ㅆ', 'ㅢ', 'ㅚ', 'ㅐ', 'ㅟ', 'ㅔ', 'ㅒ', 'ㅖ', 'ㅘ', 'ㅝ',
                       'ㅙ', 'ㅞ']

while True:
    random_letter = get_random_korean_letter()
    print(f"Write {random_letter} or 'End' to exit: ")
    command = input()
    if command.lower() == 'End':
        print("Goodbye!")
        exit()

    if command.strip() == random_letter:
        print("Correct!")
    else:
        while command != random_letter and command.lower() != 'next':
            print("Try again, write 'Next' for the next letter or write 'End' to exit")
            command = input()
            if command.lower() == 'end':
                print("Goodbye!")
                exit()
