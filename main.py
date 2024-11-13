# Dicionário de opcodes para as instruções
opcodes = {
    "ADD": "0000",
    "SUB": "0001",
    "MULT": "0010",
    "DIVISION": "0011",
    "AND": "0100",
    "OR": "0101",
    "LI": "1000", 
    "SW": "1001", 
    "LW": "1010", 
    "JUMP": "1011",
    "IF EQUAL": "1100",
    "IF LEQ": "1101",
    "STOP": "1111"
}
def save_instructions_to_file(filename, instructions):
    hex_instructions = process_instructions_to_hex(instructions)
    with open(filename, 'w') as file:
        file.write('v2.0 raw' + '\n')
        for hex_instr in hex_instructions:
            file.write(hex_instr + ' ')
def reg_to_bin(register):
    num = int(register[1:])
    return format(num, '04b')

def instruction_to_bin(instruction):
    parts = instruction.split()
    instr = parts[0]  # Nome da instrução

    if instr == "STOP": 
        return f"{opcodes[instr]} {'0000'} {'0000'} {'0000'} {'0' * 16}"

    if instr == "LI": 
        reg_bin = reg_to_bin(parts[1])
        imm_value = int(parts[2])
        imm_bin = format(imm_value, '016b')  # Valor imediato em 16 bits
        return f"{opcodes[instr]} {'0000'} {'0000'} {reg_bin} {imm_bin}"
    
    elif instr == "SW" or instr == "LW":  # Para SW e LW
        reg_x_bin = reg_to_bin(parts[1])
        reg_y_bin = reg_to_bin(parts[2])
        return f"{opcodes[instr]} {reg_x_bin} {'0000'} {reg_y_bin}  {'0' * 16}"
    
    elif instr == "JUMP":  # Para JUMP
        reg_d_bin = reg_to_bin(parts[1])
        return f"{opcodes[instr]} {reg_d_bin} {'0000'} {'0000'} {'0' * 16}"
    
    elif instr == "IF":  # Para IF EQUAL
        if_type = f"IF {parts[1]}"  # IF EQUAL ou IF LEQ
        reg_1_bin = reg_to_bin(parts[2])
        reg_2_bin = reg_to_bin(parts[3])
        reg_d_bin = reg_to_bin(parts[4])
        return f"{opcodes[if_type]} {reg_1_bin} {reg_2_bin} {reg_d_bin} {'0' * 16}"
    
    else:  # Para ADD, SUB, MULT, DIVISION, AND, OR
        reg_x_bin = reg_to_bin(parts[1])
        reg_y_bin = reg_to_bin(parts[2])
        reg_z_bin = reg_to_bin(parts[3])
        return f"{opcodes[instr]} {reg_x_bin} {reg_y_bin} {reg_z_bin} {'0' * 16}"

def process_instructions(instructions):
    result = []
    for instruction in instructions:
        result.append(instruction_to_bin(instruction))
    return result

def bin_to_hex(bin_str):
    bin_str = bin_str.replace(" ", "")
    hex_str = format(int(bin_str, 2), '08X')
    return hex_str

def process_instructions_to_hex(instructions):
    result = []
    for instruction in instructions:
        bin_instr = instruction_to_bin(instruction)
        hex_instr = bin_to_hex(bin_instr)
        result.append(hex_instr)
    return result

def read_instructions_from_file():
    with open("code.txt", 'r') as file:
        instructions = [line.strip() for line in file.readlines()]
    return instructions

instructions = read_instructions_from_file()

binary_instructions = process_instructions(instructions)
for bin_instr in binary_instructions:
    print(bin_instr)
    
filename = input("Digite o nome do arquivo para salvar (ex: instructions.txt): ")
save_instructions_to_file(filename, instructions)