def get_bags(color, data):
    rule = get_rule_from_bag_name(color, data)
    rule = rule.replace("bags contain ", "").replace("no other bags.", "").replace(", ", ",")
    print(color)

    total_bags = 0
    
    if rule != "":
        bags = rule.split(",")
    else:
        bags = []

    print(bags)

    for bag in bags:
        print(bag)
        rule_list = bag.split(" ")
        # print(rule_list)

        amount = int(rule_list[0])
        bag_name = f'{rule_list[1]} {rule_list[2]}'

        contains = get_bags(bag_name, data)
        # print(f'{bag_name} containts {contains} other bags')

        if contains > 0:
            total_bags += amount + (amount * contains)
        else:
            total_bags += amount 

    return total_bags
        

def get_rule_from_bag_name(name, data):
    for rule in data:
        rule_words = rule.split(" ")
        bag_adjective = rule_words.pop(0)
        bag_color = rule_words.pop(0)
        bag_name = f"{bag_adjective} {bag_color}"
        bag_rule = " ".join(rule_words)
        if bag_name == name:
            return bag_rule

def solve_part_1(data):
    bag_list = []
    unique_bags = []
    total_bags = 0

    for rule in data:
        rule_words = rule.split(" ")
        bag_adjective = rule_words.pop(0)
        bag_color = rule_words.pop(0)
        bag_name = f"{bag_adjective} {bag_color}"
        bag_rule = " ".join(rule_words)
        if "shiny gold" in bag_rule:
            bag_list.append(bag_name)
            if bag_name not in unique_bags:
                unique_bags.append(bag_name)

    total_bags += len(bag_list)
    
    while len(bag_list) > 0:
        new_bag_list = []
        for bag in bag_list:
            for rule in data:
                rule_words = rule.split(" ")
                bag_adjective = rule_words.pop(0)
                bag_color = rule_words.pop(0)
                bag_name = f"{bag_adjective} {bag_color}"
                bag_rule = " ".join(rule_words)
                if bag in bag_rule:
                    new_bag_list.append(bag_name)
                    if bag_name not in unique_bags:
                        unique_bags.append(bag_name)
        
        bag_list = new_bag_list
        total_bags += len(bag_list)
    
    print(f"Total Bags: {total_bags}")
    print(f"Unique Bags: {len(unique_bags)}")
   

def solve_part_2(data):
    bag_list = []
    total_bags = 0

    bags = get_bags("shiny gold", data)
    
    print(bags)   

    
if __name__ == "__main__":
    input = open('c:/Projects/advent_of_code_2020/day_7/input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('c:/Projects/advent_of_code_2020/day_7/input.txt', 'r').read().splitlines()
    solve_part_2(input_two)