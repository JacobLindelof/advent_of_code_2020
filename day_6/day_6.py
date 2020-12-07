def solve_part_1(data):
    answers = []
    answer_data = {
        "group_members": 0,
        "answers": ''
    }
    for line in data:
        if line == '':
            answers.append(answer_data)
            answer_data = {
                "group_members": 0,
                "answers": ''
            }
        else:
            answer_data['group_members'] += 1
            answer_data['answers'] += line
    answers.append(answer_data)

    sum = 0
    for group_answers in answers:
        answer_map = {}
        for answer in group_answers['answers']:
            if answer not in answer_map:
                answer_map[answer] = 0
            answer_map[answer] += 1
        
        for answer in answer_map.values():
            print(answer)
            if answer == group_answers['group_members']:
                sum += 1

    print(f"Sum: {sum}")


def solve_part_2(data):
    pass
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)