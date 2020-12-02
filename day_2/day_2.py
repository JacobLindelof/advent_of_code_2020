def solve_part_1(data):
    invalid_passwords = 0
    for password in data:
        password_data = password.replace(':', '').split(" ")

        character_range = password_data[0]
        character_min = int(character_range.split('-')[0])
        character_max = int(character_range.split('-')[1])

        required_character = password_data[1]

        text_password = password_data[2]
        char_map = {}
        for char in text_password:
            if char not in char_map.keys():
                char_map[char] = 0
            char_map[char] += 1
        
        if required_character not in char_map.keys():
            invalid_passwords += 1
            continue

        required_character_count = char_map[required_character]
        if character_min > required_character_count or character_max < required_character_count:
            invalid_passwords += 1

    print(f'Part One Answer: Valid Passwords: {len(data) - invalid_passwords}')

def solve_part_2(data):
    invalid_passwords = 0
    for password in data:
        password_data = password.replace(':', '').split(" ")

        character_range = password_data[0]
        char_position_one = int(character_range.split('-')[0]) - 1
        char_position_two = int(character_range.split('-')[1]) - 1

        required_character = password_data[1]

        text_password = password_data[2]
        
        char_in_first_position = required_character == text_password[char_position_one]
        char_in_second_position = required_character == text_password[char_position_two]

        if (char_in_first_position and char_in_second_position) or (not char_in_first_position and not char_in_second_position):
            invalid_passwords += 1

    print(f'Part One Answer: Valid Passwords: {len(data) - invalid_passwords}')
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)