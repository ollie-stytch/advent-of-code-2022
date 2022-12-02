letter_to_val = {"X": 1, "Y": 2, "Z": 3}
letter_for_me_to_win = {"A":"Y", "B":"Z", "C":"X"}
letter_to_draw = {"A":"X", "B":"Y", "C":"Z"}
letter_for_me_to_lose = {"A":"Z", "B":"X", "C":"Y"}
my_score = 0

with open('input.txt', encoding='utf8') as f:
    for line in f:
        enemy_letter = line.split()[0]
        my_letter = line.split()[1]
        my_score += letter_to_val[my_letter]
        if letter_for_me_to_win[enemy_letter] == my_letter:
            my_score += 6
        elif letter_to_draw[enemy_letter] == my_letter:
            my_score += 3

print(my_score)
