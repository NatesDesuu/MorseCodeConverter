from data import morse_code_dict

while True:
    query = input("Enter the text to be converted into Morse Code: ").lower()
    char_list, should_print = [], True
    for char in query:
        # If a character in the query string does not have a corresponding Morse Code
        if char not in morse_code_dict:
            # Inform user about it along with the character in question
            print(f"Invalid character found in text: {char}")
            should_print = False
            break
        # Append list with the Morse Code extracted from dictionary using the character as key
        char_list.append(morse_code_dict[char])
    if should_print:
        print(''.join(char_list))
