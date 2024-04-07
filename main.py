from data import morse_code_dict

while True:
    query = input("Enter the text to be converted into Morse Code: ").lower()
    char_list, should_print = [], True
    for char in query:
        if char not in morse_code_dict:
            print(f"Invalid character found in text: {char}")
            should_print = False
            break
        char_list.append(morse_code_dict[char])
    if should_print:
        print(''.join(char_list))
