from part1 import get_stack, get_stack_size, get_stack_arrays, get_instructions

def move_crates(instructions, stacks):
    for instruction in instructions:
        crates_to_move = instruction[0]
        from_stack_index = instruction[1] - 1
        to_stack_index = instruction[2] - 1
        moved_crates = []
        for _ in range(crates_to_move):
            moved_crates.append(stacks[from_stack_index].pop(0))
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