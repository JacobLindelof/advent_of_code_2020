def solve_part_1(data):
    highest_id = 0
    rows = list(range(128))
    seats = list(range(8))
    for seat_data in data:
        row_data = seat_data[:7]
        seat_data = seat_data[7:]
        
        for char in row_data:
            if char == "F":
                rows = rows[:int(len(rows) / 2)]
            else:
                rows = rows[int(len(rows) / 2):]

        for char in seat_data:
            if char == "L":
                seats = seats[:int(len(seats) / 2)]
            else:
                seats = seats[int(len(seats) / 2):]

        seat_id = rows[0] * 8 + seats[0]
        if seat_id > highest_id:
            highest_id = seat_id
        
        rows = list(range(128))
        seats = list(range(8))
    
    print(f"Largest Seat ID: {highest_id}")


def solve_part_2(data):
    ids = []
    rows = list(range(128))
    seats = list(range(8))
    for seat_data in data:
        row_data = seat_data[:7]
        seat_data = seat_data[7:]
        
        for char in row_data:
            if char == "F":
                rows = rows[:int(len(rows) / 2)]
            else:
                rows = rows[int(len(rows) / 2):]

        for char in seat_data:
            if char == "L":
                seats = seats[:int(len(seats) / 2)]
            else:
                seats = seats[int(len(seats) / 2):]

        seat_id = rows[0] * 8 + seats[0]
        ids.append(seat_id)        
        
        rows = list(range(128))
        seats = list(range(8))          
    
    ids = sorted(ids)
    current_id = ids[0]
    index = 0
    print(ids)
    for seat_id in ids:
        if seat_id != current_id:
            print(f'Missing ID: {current_id}')
            return
        current_id += 1
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)