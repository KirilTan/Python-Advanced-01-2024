import os

with open('created_for_deletion.txt', 'w') as file:
    file.write('I will be deleted in a few seconds!')

file = 'created_for_deletion.txt'
os.remove(file)
