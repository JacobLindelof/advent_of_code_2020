from collections import defaultdict

def solve_part_1(data):
    rules = defaultdict(lambda: {
        "possible_indexes": defaultdict(int),
        "valid_indexes": [],
        "ticket_index": None,
        "ranges": []
    })

    rule = data.pop(0)

    while rule != "":
        rule_data = rule.replace(": ", ":").replace(" or ", ":").split(":")
        rule_text = rule_data[0]
        rule_range_1 = rule_data[1].split("-")
        rule_range_2 = rule_data[2].split("-")

        rules[rule_text]['ranges'].append({
            "min": int(rule_range_1[0]),
            "max": int(rule_range_1[1])
        })

        rules[rule_text]['ranges'].append({
            "min": int(rule_range_2[0]),
            "max": int(rule_range_2[1])
        })

        rule = data.pop(0)
    
    data.pop(0)
    my_ticket_list = data.pop(0).split(',')
    my_ticket = []
    for num in my_ticket_list:
        my_ticket.append(int(num))

    data.pop(0)
    data.pop(0)

    valid_tickets = []
    invalid_tickets = []

    invalid_values = 0

    for string in data:
        ticket = []
        for number in string.split(','):
            ticket.append(int(number))
        
        ticket_valid = True
        for value in ticket:
            value_valid = False
            for rule in rules.values():
                if (value >= rule['ranges'][0]["min"] and value <= rule['ranges'][0]["max"]) or (value >= rule['ranges'][1]["min"] and value <= rule['ranges'][1]["max"]):
                    value_valid = True

            if not value_valid:
                invalid_values += value
                ticket_valid = False

        if ticket_valid:
            valid_tickets.append(ticket)
        else:
            invalid_tickets.append(ticket)
    
    print("Error Rate: " + str(invalid_values))

    print(f'Valid Tickets: {len(valid_tickets)}')
    for ticket in valid_tickets:
        index = 0
        for value in ticket:
            for rule in rules.values():
                if (value >= rule['ranges'][0]["min"] and value <= rule['ranges'][0]["max"]) or (value >= rule['ranges'][1]["min"] and value <= rule['ranges'][1]["max"]):
                    rule['possible_indexes'][index] += 1
            index += 1
    
    for rule, data in rules.items():
        for index, possible_index in data['possible_indexes'].items():
            if possible_index == len(valid_tickets):
                data['valid_indexes'].append(index)

    ticket_indexes = {}
    while len(ticket_indexes) < len(rules):
        for rule, data in rules.items():
            if len(data['valid_indexes']) == 1:
                index = data['valid_indexes'][0]
                data['ticket_index'] = index
                ticket_indexes[rule] = index
                for rule in rules.values():
                    if index in rule['valid_indexes']:
                        rule['valid_indexes'].pop(rule['valid_indexes'].index(index))
    
    value = None
    for rule, index in ticket_indexes.items():
        if "departure" in rule:
            if not value:
                value = my_ticket[index]
            else:
                value = value * my_ticket[index]

    print(f'Ticket Value: {value}')


def solve_part_2(data):
    pass
    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)