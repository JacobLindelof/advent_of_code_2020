import copy

def process_seat_changes(rows):
    original_rows = copy.deepcopy(rows)
    new_rows = copy.deepcopy(rows)

    min_x, min_y, max_x, max_y = 0, 0, len(original_rows[0]) - 1, len(original_rows) - 1
    for x in range(len(original_rows[0])):
        for y in range(len(original_rows)):
            seat_to_check = original_rows[y][x]              
            
            seats = []
            seats.append([y-1, x-1])
            seats.append([y-1, x])
            seats.append([y-1, x+1])
            seats.append([y, x+1])
            seats.append([y+1, x+1])
            seats.append([y+1, x])
            seats.append([y+1, x-1])
            seats.append([y, x-1])
            
            occupied_seats = 0
            for seat in seats:
                if seat[0] >= min_y and seat[0] <= max_y and seat[1] >= min_x and seat[1] <= max_x:
                    if original_rows[seat[0]][seat[1]] == "#":
                        occupied_seats += 1

            if occupied_seats == 0 and seat_to_check == 'L':
                new_rows[y][x] = "#"
            elif occupied_seats >= 4 and seat_to_check == "#":
                new_rows[y][x] = "L"      

    return new_rows


def solve_part_1(data):
    rows = []
    for row in data:
        seat_row = []
        for seat in row:
            seat_row.append(seat)
        rows.append(seat_row)

    new_rows = process_seat_changes(rows)

    while new_rows != rows:
        rows = copy.deepcopy(new_rows)
        new_rows = process_seat_changes(rows)

    occupied_seats = 0
    for row in new_rows:
        for seat in row:
            if seat == "#":
                occupied_seats += 1
    
    print(f'Occupied Seats: {occupied_seats}')


def find_visible_adjacent_seats(seat_y, seat_x, new_y, new_x, max_y, max_x, original_rows):
    y_direction = new_y - seat_y
    x_direction = new_x - seat_x
    
    seat_y = new_y
    seat_x = new_x
    
    new_y = new_y + y_direction
    new_x = new_x + x_direction
    seat = [new_y, new_x]
    if seat[0] >= 0 and seat[0] <= max_y and seat[1] >= 0 and seat[1] <= max_x:
        if original_rows[seat[0]][seat[1]] == "#":
            return original_rows[seat[0]][seat[1]]
        elif original_rows[seat[0]][seat[1]] == ".":
            return find_visible_adjacent_seats(seat_y, seat_x, new_y, new_x, max_y, max_x, original_rows)
    return None

    

def process_seat_changes_visible_seats(rows):
    original_rows = copy.deepcopy(rows)
    new_rows = copy.deepcopy(rows)

    min_x, min_y, max_x, max_y = 0, 0, len(original_rows[0]) - 1, len(original_rows) - 1
    for x in range(len(original_rows[0])):
        for y in range(len(original_rows)):
            seat_to_check = original_rows[y][x]              
            
            seats = []
            seats.append([y-1, x-1])
            seats.append([y-1, x])
            seats.append([y-1, x+1])
            seats.append([y, x+1])
            seats.append([y+1, x+1])
            seats.append([y+1, x])
            seats.append([y+1, x-1])
            seats.append([y, x-1])
            
            occupied_seats = 0
            for seat in seats:
                if seat[0] >= min_y and seat[0] <= max_y and seat[1] >= min_x and seat[1] <= max_x:
                    if original_rows[seat[0]][seat[1]] == "#":
                        occupied_seats += 1
                    elif original_rows[seat[0]][seat[1]] == ".":
                        visible_seat = find_visible_adjacent_seats(y, x, seat[0], seat[1], max_y, max_x, original_rows)
                        if visible_seat != None and visible_seat == "#":
                            occupied_seats += 1
                    

            if occupied_seats == 0 and seat_to_check == 'L':
                new_rows[y][x] = "#"
            elif occupied_seats >= 5 and seat_to_check == "#":
                new_rows[y][x] = "L"      

    return new_rows

def solve_part_2(data):
    rows = []
    for row in data:
        seat_row = []
        for seat in row:
            seat_row.append(seat)
        rows.append(seat_row)

    new_rows = process_seat_changes_visible_seats(rows)

    while new_rows != rows:
        rows = copy.deepcopy(new_rows)
        new_rows = process_seat_changes_visible_seats(rows)

    occupied_seats = 0
    for row in new_rows:
        for seat in row:
            if seat == "#":
                occupied_seats += 1
    
    print(f'Occupied Seats: {occupied_seats}')
    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)