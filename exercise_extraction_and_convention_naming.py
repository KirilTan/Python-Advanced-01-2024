import re

regex = r"([0-9]{1,2}.	([A-z]+ )+[A-z]+)"

test_str = (input())

matches = re.finditer(regex, test_str, re.MULTILINE)

# Extracting matches into a list
matches_list = [match.group() for match in matches]

# Replace '\t' (tab character) with an empty string in each match
matches_list = [match.replace('\t', '') for match in matches_list]

print(matches_list)
