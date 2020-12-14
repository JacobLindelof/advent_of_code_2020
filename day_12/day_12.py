def solve_part_1(data):
    pos_y = 0
    pos_x = 0
    
    ship_directions = ["E", "S", "W", "N",] * 100
    direction_index = 200
    ship_facing = ship_directions[direction_index]

    for instruction in data:
        direction, distance = instruction[0], int(instruction[1:])
        
        if direction == "F": 
            direction = ship_facing
        
        if direction == "N":
            pos_y -= distance
        elif direction == "S":
            pos_y += distance     
        elif direction == "W":
            pos_x -= distance      
        elif direction == "E":
            pos_x += distance

        if direction == "R":
            distance = int(distance / 90)
            direction_index += distance
            ship_facing = ship_directions[direction_index]

        if direction == "L":
            distance = int(distance / 90)
            direction_index -= distance
            ship_facing = ship_directions[direction_index]
    
    if pos_x < 0:
        pos_x = pos_x * -1
    
    if pos_y < 0:
        pos_y = pos_y * -1
    
    print(f"Final Ship Position: ({pos_x}, {pos_y}) | Manhattan Distance: {pos_x + pos_y}")


def solve_part_2(data):
    pos_y = 0
    pos_x = 0

    waypoint_y = 1
    waypoint_x = 10
    
    ship_directions = ["E", "S", "W", "N",] * 100
    direction_index = 200
    ship_facing = ship_directions[direction_index]

    for instruction in data:
        direction, distance = instruction[0], int(instruction[1:])
        
        if direction == "F": 
            pos_x += waypoint_x * distance
            pos_y += waypoint_y * distance
        
        if direction == "N":
            waypoint_y += distance
        elif direction == "S":
            waypoint_y -= distance     
        elif direction == "W":
            waypoint_x -= distance      
        elif direction == "E":
            waypoint_x += distance

        if direction in ["L", "R"]:
            distance = int(distance / 90)

            for i in range(distance):
                print(i)
                if direction == "R":
                    old_waypoint_x = waypoint_x
                    old_waypoint_y = waypoint_y

                    waypoint_x = old_waypoint_y
                    waypoint_y = old_waypoint_x * -1
                else: 
                    old_waypoint_x = waypoint_x
                    old_waypoint_y = waypoint_y

                    waypoint_x = old_waypoint_y * -1
                    waypoint_y = old_waypoint_x
        
        print(f"Direction: {direction}, Distance: {distance}, X: {pos_x}, Y: {pos_y}, WX: {waypoint_x}, WY: {waypoint_y}")

                
    if pos_x < 0:
        pos_x = pos_x * -1
    
    if pos_y < 0:
        pos_y = pos_y * -1
    
    print(f"Final Ship Position: ({pos_x}, {pos_y}) | Manhattan Distance: {pos_x + pos_y}")


if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)