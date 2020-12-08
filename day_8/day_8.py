def check_for_loop(instructions):
    accumulator = 0
    executed_instructions = []

    current_instruction = 0
    infinite_loop = False

    while not infinite_loop:
        if current_instruction in executed_instructions:
            infinite_loop = True
            return True
        elif current_instruction == len(instructions):
            return False
        else:
            executed_instructions.append(current_instruction)

        instruction = instructions[current_instruction]
        if "acc" in instruction:
            if "+" in instruction:
                accumulator += int(instruction.replace("acc +", ""))
            else:
                accumulator -= int(instruction.replace("acc -", ""))
            current_instruction += 1
        elif "jmp" in instruction:
            if "+" in instruction:
                current_instruction += int(instruction.replace("jmp +", ""))
            else:
                current_instruction -= int(instruction.replace("jmp -", ""))
        else:
            current_instruction += 1


def execute_instructions(instructions):
    accumulator = 0
    executed_instructions = []
    current_instruction = 0

    while True:
        if current_instruction == len(instructions):
            return accumulator
        else:
            executed_instructions.append(current_instruction)

        instruction = instructions[current_instruction]
        if "acc" in instruction:
            if "+" in instruction:
                accumulator += int(instruction.replace("acc +", ""))
            else:
                accumulator -= int(instruction.replace("acc -", ""))
            current_instruction += 1
        elif "jmp" in instruction:
            if "+" in instruction:
                current_instruction += int(instruction.replace("jmp +", ""))
            else:
                current_instruction -= int(instruction.replace("jmp -", ""))
        else:
            current_instruction += 1

def solve_part_1(data):
    instructions = list(data)
    accumulator = 0
    executed_instructions = []

    current_instruction = 0
    infinite_loop = False

    while not infinite_loop:
        if current_instruction in executed_instructions:
            infinite_loop = True
            continue
        else:
            executed_instructions.append(current_instruction)

        executed_instructions.append(current_instruction)
        instruction = instructions[current_instruction]
        if "acc" in instruction:
            if "+" in instruction:
                accumulator += int(instruction.replace("acc +", ""))
            else:
                accumulator -= int(instruction.replace("acc -", ""))
            current_instruction += 1
        elif "jmp" in instruction:
            if "+" in instruction:
                current_instruction += int(instruction.replace("jmp +", ""))
            else:
                current_instruction -= int(instruction.replace("jmp -", ""))
        else:
            current_instruction += 1
            
    print(f"Accumulator Value: {accumulator}")

   

def solve_part_2(data):
    instruction_set = data
    loop = check_for_loop(instruction_set)
    for i in range(len(instruction_set)):
        if "nop" in instruction_set[i]:
            instruction_set[i] = instruction_set[i].replace("nop", "jmp")
            loop = check_for_loop(instruction_set)
            if loop:
                instruction_set[i] = instruction_set[i].replace("jmp", "nop")
            else:
                accumulator = execute_instructions(instruction_set)
                print(f"Accumulator Value: {accumulator}")
                return

        elif "jmp" in instruction_set[i]:
            instruction_set[i] = instruction_set[i].replace("jmp", "nop")
            loop = check_for_loop(instruction_set)
            if loop:
                instruction_set[i] = instruction_set[i].replace("nop", "jmp")
            else:
                accumulator = execute_instructions(instruction_set)
                print(f"Accumulator Value: {accumulator}")
                return


    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)