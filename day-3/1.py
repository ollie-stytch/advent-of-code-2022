def get_compartments(line):
    clean_line = line.strip()
    midpoint = (int(len(clean_line) / 2))
    comp_one, comp_two = clean_line[: midpoint], clean_line[midpoint:]
    comp_one_list, comp_two_list = [],[]
    comp_one_list[:0], comp_two_list[:0] = comp_one, comp_two
    return set(comp_one_list), set(comp_two_list)

def convert_letter_to_points(letter):
    if letter.islower():
        return ord(letter) - 97 + 1
    else:
        return ord(letter) - 65 + 26 + 1

points_sum = 0

with open('input.txt', encoding='utf8') as f:
    for line in f:
      line = line.strip()
      comp_one, comp_two = get_compartments(line)
      print(comp_one.intersection(comp_two))
      letter = next(iter(comp_one & comp_two))
      points = convert_letter_to_points(letter)
      print(points)
      points_sum += points
      

print(points_sum)
