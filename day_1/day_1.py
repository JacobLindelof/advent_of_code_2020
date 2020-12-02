def solve_part_1(data):
    while len(data) > 0:
        first_number = int(data.pop(0))
        for number in data:
            second_number = int(number)
            if (first_number + second_number) == 2020:
                print(f'Part 1 Answer: {first_number * second_number}')
                return

def solve_part_2(data):
    while len(data) > 0:
        first_number = int(data.pop(0))
        for i in range(len(data) - 1):
            second_number = int(data[i])
            for i in range(len(data) - 1):
                third_number = int(data[i + 1])
                if (first_number + second_number + third_number) == 2020:
                    print(f'Part 2 Answer: {first_number * second_number * third_number}')
                    return
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)