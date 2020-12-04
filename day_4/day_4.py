import string

def solve_part_1(data):
    passports = []
    passport_data = []
    for line in data:
        if line == '':
            passports.append(passport_data)
            passport_data = []
        else:
            data = line.split(" ")
            for data_point in data:
                passport_data.append(data_point)
    passports.append(passport_data)

    valid_passports = 0
    for passport in passports:
        passport_dictionary = {}
        for data in passport:
            data = data.split(":")
            passport_dictionary[data[0]] = data[1]

        byr = "byr" in passport_dictionary.keys() and int(passport_dictionary['byr']) >= 1920 and int(passport_dictionary['byr']) <= 2002
        iyr = "iyr" in passport_dictionary.keys() and int(passport_dictionary['iyr']) >= 2010 and int(passport_dictionary['iyr']) <= 2020
        eyr = "eyr" in passport_dictionary.keys() and int(passport_dictionary['eyr']) >= 2020 and int(passport_dictionary['eyr']) <= 2030
        hgt = "hgt" in passport_dictionary.keys()
        hcl = "hcl" in passport_dictionary.keys() and passport_dictionary['hcl'][0] == '#'
        ecl = "ecl" in passport_dictionary.keys() and passport_dictionary['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = "pid" in passport_dictionary.keys() and len(passport_dictionary['pid']) == 9 and passport_dictionary['pid'].isdigit()
        cid = "cid" in passport_dictionary.keys()

        if hgt: 
            height_string = passport_dictionary['hgt']
            if "in" in height_string:
                height_string = height_string.replace("in", "")
                try:
                    height = int(height_string)
                    hgt = True if height >= 59 and height <= 76 else False
                except:
                    hgt = False
            elif "cm" in height_string:
                height_string = height_string.replace("cm", "")
                try:
                    height = int(height_string)
                    hgt = True if height >= 150 and height <= 193 else False
                except:
                    hgt = False
            else:
                hgt = False

        if hcl:
            for char in passport_dictionary['hcl']:
                if char not in ["#", '0', "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
                    hcl = False
        

        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid_passports += 1

    print(f'Total Passports: {len(passports)} | Valid Passports: {valid_passports}| Invalid Passports: {len(passports) - valid_passports}')

def solve_part_2(data):
    pass
    
if __name__ == "__main__":
    input = open('input.txt', 'r').read().splitlines()
    solve_part_1(input)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)