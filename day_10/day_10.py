def solve_part_1(data):
    jolt_difference_of_1 = 0
    jolt_difference_of_3 = 0
    adapters = []
    for x in data.copy():
        adapters.append(int(x))
    adapters = sorted(adapters)

    if adapters[0] == 1:
        jolt_difference_of_1 += 1
    else:
        jolt_difference_of_3 += 1

    for y in range(len(adapters)):
        if y != len(adapters) - 1 and adapters[y] + 1 == adapters[y + 1]:
            jolt_difference_of_1 += 1
        else:
            jolt_difference_of_3 += 1
    
    print(f'1 Jolt: {jolt_difference_of_1} | 3 Jolt: {jolt_difference_of_3} | Product: {jolt_difference_of_1 * jolt_difference_of_3}')

def solve_part_2(data):
    pass

    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)