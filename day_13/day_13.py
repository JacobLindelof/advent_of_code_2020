def solve_part_1(data):
    departure_time = int(data[0])
    bus_lines = []
    for bus in data[1].split(','):
        if bus != "x":
            bus_lines.append(int(bus))

    possible_times = {}
    for line in bus_lines:
        line_number = line
        while True:
            line += line_number
            if line > departure_time:
                possible_times[line_number] = line
                break

    lowest_bus = None
    lowest_time = None
    for bus, time in possible_times.items():
        if lowest_time == None or time < lowest_time:
            lowest_time = time
            lowest_bus = bus
    
    lowest_wait_time = lowest_time - departure_time
    print(f'Answer: {lowest_wait_time * lowest_bus}')


def check_valid(start_time, bus_lines):
    valid = True
    for i in range(len(bus_lines)):
        if i != 0:
            if bus_lines[i] is not None:
                if (start_time + i) % bus_lines[i] != 0:
                    return False
    if valid == True:
        print(f'Earliest Solution: {start_time}')
        return True


def solve_part_2(data):
    bus_lines = []
    for bus in data[1].split(','):
        if bus != "x":
            bus_lines.append(int(bus))
        else:
            bus_lines.append(None)

    start_time = 725850285300475
    loop_number = 0
    while True:
        valid = check_valid(start_time, bus_lines)
        if valid:
            return
        start_time += bus_lines[0]



if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('example.txt', 'r').read().splitlines()
    solve_part_2(input_two)