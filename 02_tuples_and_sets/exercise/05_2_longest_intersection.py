number_of_inputs = int(input())

intersections = []
for _ in range(number_of_inputs):
    first_range, second_range = input().split('-')
    first_start, first_end = map(int, first_range.split(','))
    second_start, second_end = map(int, second_range.split(','))

    first_range_numbers = set(range(first_start, first_end + 1))
    second_range_numbers = set(range(second_start, second_end + 1))

    intersection = first_range_numbers.intersection(second_range_numbers)
    intersections.append(intersection)

longest_intersection = ()
for intersection in intersections:
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection


print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")
