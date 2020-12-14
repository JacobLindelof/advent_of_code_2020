def solve_part_1(data):
    memory_register = {}
    mask = None
    for row in data:
        if "mask" in row:
            mask = row.replace('mask = ', '')
        else:
            address, value = row.replace('mem[', '').replace('] = ', ':').split(':')
            address = int(address)
            value = [char for char in bin(int(value)).replace('0b', '')[::-1]]

            new_value = [char for char in mask[::-1]]
            for i in range(len(value)):
                if new_value[i] == 'X':
                    new_value[i] = value[i]
            
            value_to_write = ''.join(new_value)[::-1].replace("X", "0")
            
            memory_register[address] = value_to_write
    
    value_total = 0
    for address, value in memory_register.items():
        value_total += int(value, 2) 

    print(f'Register Total: {value_total}')

def get_memory_addresses(address_to_flip, bits, starting_address=None):
    addresses = []

    new_address_to_flip = []

    if starting_address:
        address_flip_0 = starting_address.copy()
        address_flip_0[bits[0]] = 0
        addresses.append(address_flip_0)
        address_flip_1 = starting_address.copy()
        address_flip_1[bits[0]] = 1
        addresses.append(address_flip_1)
    else:
        for address in address_to_flip:
            address_flip_0 = address.copy()
            address_flip_0[bits[0]] = 0
            addresses.append(address_flip_0)
            address_flip_1 = address.copy()
            address_flip_1[bits[0]] = 1
            addresses.append(address_flip_1)

    bits.pop(0)
    if len(bits) > 0:
        addresses = get_memory_addresses(addresses, bits)

    return addresses

def solve_part_2(data):
    memory_register = {}
    mask = None
    for row in data:
        if "mask" in row:
            mask = row.replace('mask = ', '')
        else:
            address, value = row.replace('mem[', '').replace('] = ', ':').split(':')
            address = [char for char in bin(int(address)).replace('0b', '')[::-1]]
            value = int(value)

            address_mask = [char for char in mask[::-1]]
            
            for i in range(len(address)):
                if address_mask[i] == "0":
                    address_mask[i] = address[i]
            
            floating_bits = []
            for i in range(len(address_mask)):
                if address_mask[i] == "X":
                    floating_bits.append(i)

            addresses_to_write = get_memory_addresses([], floating_bits, address_mask)   
            
            for address in addresses_to_write:
                address = int(''.join(str(x) for x in address)[::-1], 2)
                memory_register[address] = value
                    
    value_total = 0
    for address, value in memory_register.items():
        value_total += value 

    print(f'Register Total: {value_total}')
    
if __name__ == "__main__":
    input_one= open('input.txt', 'r').read().splitlines()
    solve_part_1(input_one)
    input_two= open('input.txt', 'r').read().splitlines()
    solve_part_2(input_two)