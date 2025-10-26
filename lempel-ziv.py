def process_input_string(input_str):
    visited = []
    alphabet = {}  # a dictionary to store characters that are given as input
    count = 0

    for k in input_str:
        if k not in alphabet:
            alphabet[k] = count
            count += 1

    i = 0
    while i < len(input_str):
        if input_str[i] in visited:
            st = input_str[i]
            j = i + 1
            while j < len(input_str) and st in visited:
                st += input_str[j]
                j += 1
            visited.append(st)
            i += len(st)
        elif input_str[i] not in visited:
            visited.append(input_str[i])
            i += 1

    print("Visited segments:", visited)

    # ----- ASCII value representation -----
    values = [''] * len(visited)
    for i in visited:
        if len(i) > 1:
            prefix = i[:-1]  # Prefix (without the last character)
            suffix = i[-1]
            prefix_index = visited.index(prefix) + 1
            suffix_ascii = str(ord(suffix))  # Get ASCII code of the suffix
            values[visited.index(i)] = str(prefix_index) + suffix_ascii
        elif len(i) == 1:
            values[visited.index(i)] = str(ord(i))  # Single character ASCII value

    print("Position values (ASCII):", values)

    # ----- Binary value representation -----
    values = [''] * len(visited)
    for i in visited:
        if len(i) > 1:
            prefix = i[:-1]
            suffix = i[-1]
            prefix_index = visited.index(prefix) + 1
            suffix_ascii = bin(ord(suffix))[2:]  # Binary representation of the suffix
            values[visited.index(i)] = bin(prefix_index)[2:] + suffix_ascii
        elif len(i) == 1:
            values[visited.index(i)] = bin(ord(i))[2:]  # Single character binary ASCII

    print("Position values (binary):", values)

    # ----- Final code word -----
    final_code_word = ''.join(values)
    print("Final Code word:", final_code_word)


if __name__ == "__main__":
    try:
        with open("text.txt", 'r') as file:
            input_string = file.read()
            process_input_string(input_string)
    except FileNotFoundError:
        print("File not found.")

