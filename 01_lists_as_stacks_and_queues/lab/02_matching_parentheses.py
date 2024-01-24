input_text = str(input())
par_stack = []

for index in range(len(input_text)):
    if input_text[index] == "(":
        par_stack.append(index)
    elif input_text[index] == ")":
        start_index = par_stack.pop()
        end_index = index + 1
        print(input_text[start_index:end_index])
