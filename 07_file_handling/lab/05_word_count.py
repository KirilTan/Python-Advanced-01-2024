import os
import re

words_to_find_path = os.path.join('words.txt')
text_to_search_path = os.path.join('input.txt')
output_file_path = os.path.join('output.txt')


with open(words_to_find_path, 'r') as file:
    searched_words = file.read().split()
    searched_words = [word.lower() for word in searched_words]

with open(text_to_search_path, 'r') as file:
    content = file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    results = re.findall(pattern, content)
    words_count[searched_word] = len(results)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file_path, 'w') as file:
    for word, count in sorted_words_count:
        file.write(f'{word} - {count} time/s\n')
