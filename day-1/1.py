max_elf_sum = -1
elf_sum = 0
elf_num = 1

with open('input.txt', encoding='utf8') as f:
    for line in f:
        if line.strip() == '': 
          max_elf_sum = max(elf_sum, max_elf_sum)
          elf_sum = 0
          elf_num += 1
          
        else:
          elf_sum += int(line)

print(max_elf_sum)
