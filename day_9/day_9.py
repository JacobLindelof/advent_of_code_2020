def check_for_sums(preamble, used_values, number):
    number = int(number)
    while len(preamble) > 0:
        x = int(preamble.pop(0))
        for y in range(len(preamble)):
            z = int(preamble[y])
            if x + z == number and x != z:
                return z
    return False    

def solve_part_1(data):
    used_values = []
    while True:
        preamble = data[:25]
        number = data[25]

        valid = check_for_sums(preamble, used_values ,number)
        if valid is not False:
            used_values.append(valid)
            data.pop(0)
        else: 
            print(f"Invalid Number: {number}")
            return int(number)

def solve_part_2(data):
    target_value = solve_part_1(data.copy())
    series_numbers = []
    series_value = 0
    while True:
        for number in data:
            series_value += int(number)
            series_numbers.append(int(number))
            if series_value == target_value:
                print(f'{series_value} | {target_value}')
                series_numbers = sorted(series_numbers)
                min_value = series_numbers[0]
                max_value = series_numbers[-1]
                print(f'Minimum: {min_value} | Maximum: {max_value} | Sum: {min_value + max_value}')

                return True
            elif series_value > target_value:
                series_value = 0
                series_numbers = []
                data.pop(0)
                break




    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)