def solve_part_1(data):
    row_length = len(data[0]) - 1
    pos_x = 0
    pos_y = 0

    trees_encountered = 0
    while pos_y < len(input) - 1:
        pos_y += 1
        pos_x += 3
        if pos_x > row_length:
            pos_x -= row_length + 1
        trees_encountered += 1 if data[pos_y][pos_x] == '#' else 0

    print(trees_encountered)

def slope_checker(x, y, data):
    row_length = len(data[0]) - 1
    pos_x = 0
    pos_y = 0

    trees_encountered = 0
    while pos_y < len(input) - 1:
        pos_y += y
        pos_x += x
        if pos_x > row_length:
            pos_x -= row_length + 1
        trees_encountered += 1 if data[pos_y][pos_x] == '#' else 0

    return trees_encountered

def solve_part_2(data):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    results = []
    for slope in slopes:
        results.append(slope_checker(slope[0], slope[1], data))

    result = 1
    for x in results:
        result = x * result
    
    print(result)
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)