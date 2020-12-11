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

def count_options(index, nodes, lookup):
    result = 0

    indexes_to_visit = []
    if index not in lookup:
        for i in range(index + 1, index + 4):
            if i < len(nodes):
                if nodes[i] - nodes[index] in (1, 2, 3):
                    indexes_to_visit.append(i)
            else:
                break

        if indexes_to_visit:
            for index_to_visit in indexes_to_visit:
                result += count_options(index_to_visit, nodes, lookup)
                lookup[index] = result
        else:
            return 1
    return lookup[index]

def solve_part_2(data):
    adapters = []
    for x in data.copy():
        adapters.append(int(x))
    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)
    adapters.insert(0, 0)
    lookup = {}

    print(count_options(0, adapters, lookup))

    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)