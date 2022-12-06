def get_lines():
    lines = []
    with open('input.txt', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    return lines

def set_starting_values(window_start, window_end, line):
    chars = {}
    for i in range(window_start, window_end):
        if line[i] in chars:
            chars[line[i]] += 1
        else:
            chars[line[i]] = 1
    return chars

def get_ans():
    line = get_lines()[0]
    window_start = 0
    window_end = 4
    chars = set_starting_values(window_start, window_end, line)

    while window_end < len(line):
        if len(chars) == 4:
            break
        
        # Decrement chars at window_start
        chars[line[window_start]] -= 1
        if chars[line[window_start]] == 0:
            del chars[line[window_start]]
        
        # Increment chars at window_end
        if line[window_end] not in chars:
            chars[line[window_end]] = 0
        chars[line[window_end]] += 1
        
        window_start += 1
        window_end += 1

    return window_end

if __name__ == "__main__":
    ans = get_ans()
    print(ans)
        