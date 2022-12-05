def get_lines():
    lines = []
    with open('input.txt', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            print(line)
            lines.append(line)
    return lines

def is_contained(e1_start, e1_end, e2_start, e2_end):
    if e1_start >= e2_start and e1_start <= e2_end and e1_end <= e2_end and e1_end >= e2_start:
        return True
    return False

if __name__ == "__main__":
    lines = get_lines()
    num_contained_pairs = 0
    for line in lines:
        e1_start = int(line.split(',')[0].split('-')[0])
        e1_end = int(line.split(',')[0].split('-')[1])
        e2_start = int(line.split(',')[1].split('-')[0])
        e2_end = int(line.split(',')[1].split('-')[1])
        if is_contained(e1_start, e1_end, e2_start, e2_end) or is_contained(e2_start, e2_end, e1_start, e1_end):
            num_contained_pairs += 1
    print(num_contained_pairs)
