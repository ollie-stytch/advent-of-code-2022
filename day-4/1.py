starting_positions = [
["R","N","F","V","L", "J", "W","M"],
["P", "N", "D", "Z", "F", "J", "W", "H"],
["W", "R", "C", "D", "G"],
["N", "B", "S"],
["M", "Z", "W", "P", "C", "B", "F", "N"],
["P", "R", "M", "W"],
["R", "T", "N", "G", "L", "S", "W"],
["Q", "T", "H", "F", "N", "B", "V"],
["L", "M", "H", "Z", "N","F"]
]

def get_lines(filename):
    lines = []
    with open(filename, encoding='utf8') as f:
        for line in f:
            line = line.strip()
            print(line)
            lines.append(line)
    return lines

def print_answer():
    for i in range(len(starting_positions)):
        print(starting_positions[i][len(starting_positions[i]) - 1])

def make_move(quantity, starting_block, ending_block):
    for i in range(quantity):
        starting_positions[ending_block - 1].append(starting_positions[starting_block - 1].pop())

if __name__ == "__main__":
    moves = get_lines("moves.txt")
    for move in moves:
        quantity = int(move.split(' ')[1])
        starting_block = int(move.split(' ')[3])
        ending_block = int(move.split(' ')[5])
        make_move(quantity, starting_block, ending_block)
    print_answer()
        
