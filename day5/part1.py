
def get_stack_size(file_name):
    with open(file_name, "r") as file:
        count = -1
        for line in file:
            count += 1
            if line == "\n":
                break
    return count

def get_stack_arrays(file_name, stack_size):
    stack_arrays = []
    with open(file_name, "r") as file:
        stacks = [next(file) for _ in range(stack_size)]
        for stack in stacks:
            to_array = [character for character in stack]
            stack_arrays.append(to_array[1::4])
    return stack_arrays

def get_stack(stacks):
    new_stack = []
    for stack in stacks:
        try:
            new_stack.append(stack.pop(0))
        except:
            pass
    new_stack = list(filter((" ").__ne__, new_stack))
    new_stack.pop(-1)
    return new_stack

def get_instructions(file_name, stack_size):
    with open(file_name, "r") as file:
        lines = file.readlines()
        instructions = lines[stack_size + 1 :]
        stripped_instructions = [instruction.strip() for instruction in instructions]
    instruction_numbers = []
    for instruction in stripped_instructions:
        f_index =instruction.find("f")
        m_index = f_index + 4
        t_index = instruction.find("t")
        o_index = t_index + 2
        instruction_numbers.append([
            int(instruction[4 : f_index]), 
            int(instruction[m_index : t_index]), 
            int(instruction[o_index :])
            ])
    return instruction_numbers

def move_crates(instructions, stacks):
    for instruction in instructions:
        crates_to_move = instruction[0]
        from_stack_index = instruction[1] - 1
        to_stack_index = instruction[2] - 1
        moved_crates = []
        for _ in range(crates_to_move):
            moved_crates.append(stacks[from_stack_index].pop(0))
        moved_crates.reverse()
        stacks[to_stack_index] = moved_crates + stacks[to_stack_index]
    return stacks

if __name__ == "__main__":
    file_name = "day5/input.txt"
    stack_size = get_stack_size(file_name)
    raw_stacks = get_stack_arrays(file_name, stack_size)
    real_stacks = [get_stack(raw_stacks) for _ in raw_stacks]
    instructions = get_instructions(file_name, stack_size)
    moved_crates = move_crates(instructions, real_stacks)
    solution = ""
    for _ in range(len(moved_crates)):
        solution += moved_crates[_][0]
    print(solution)
    