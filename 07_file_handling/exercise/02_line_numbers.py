from string import punctuation

with open('text_2.txt', 'r') as file:
    text = file.readlines()

with open('output.txt', 'w') as output_file:
    for row in range(len(text)):
        letters, punctuation_marks = 0, 0

        for symbol in text[row]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                punctuation_marks += 1

        output_file.write(f'Line {row + 1} {text[row][:-1]}'
                          f'\nLetters: ({letters}) '
                          f'\nPunctuation marks: ({punctuation_marks})'
                          f'\n\n')
