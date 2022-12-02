decision_to_points = {"X": 0, "Y": 3, "Z": 6}
letter_to_val = {"X": 1, "Y": 2, "Z": 3}
letter_for_me_to_win = {"A":"Y", "B":"Z", "C":"X"}
letter_to_draw = {"A":"X", "B":"Y", "C":"Z"}
letter_for_me_to_lose = {"A":"Z", "B":"X", "C":"Y"}
my_score = 0

with open('input.txt', encoding='utf8') as f:
    for line in f:
        enemy_letter = line.split()[0]
        my_letter = line.split()[1]
        my_score += decision_to_points[my_letter]

        # Lose
        if my_letter == "X":  
          my_score += letter_to_val[letter_for_me_to_lose[enemy_letter]]

        # Draw
        if my_letter == "Y":  
          my_score += letter_to_val[letter_to_draw[enemy_letter]]

        # Win
        if my_letter == "Z":  
          my_score += letter_to_val[letter_for_me_to_win[enemy_letter]]

print(my_score)
