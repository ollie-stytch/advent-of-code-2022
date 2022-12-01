elf_sum = 0
arr = []

with open('input.txt', encoding='utf8') as f:
    for line in f:
        if line.strip() == '': 
          arr.append(elf_sum)
          elf_sum = 0
          
        else:
          elf_sum += int(line)

arr.sort()
print(arr[-1], arr[-2], arr[-3]) 
print(arr[-1] + arr[-2] + arr[-3])
