f = open("input_day2.txt", "r")
### PART ONE
content = f.readlines()
total_points = 0 # stores the total points
counter = 0
win_condition = ["A Y", "B Z", "C X"]
draw_condition = ["A X", "B Y", "C Z"]
for line in content:
    if any(x in line for x in win_condition):
        total_points += 6
    elif any(x in line for x in draw_condition):
        total_points += 3
    else:
        # not necessary
        total_points += 0
    if "X" in line:
        total_points += 1
    elif "Y" in line:
        total_points += 2
    elif "Z" in line: # or else
        total_points += 3
print(total_points)
"""
### PART ONE
# First attempt. Not pretty.

total_points = 0
for line in content:
    if "A Y" in line:
        total_points += 6 + 2
        counter += 1
    elif "A X" in line:
        total_points += 3 + 1
        counter += 1
    elif "A Z" in line:
        total_points += 0 + 3
        counter += 1

    if "B Z" in line:
        total_points += 6 + 3
        counter += 1
    elif "B Y" in line:
        total_points += 3 + 2
        counter += 1
    elif "B X" in line:
        total_points += 0 + 1
        counter += 1

    if "C X" in line:
        total_points += 6 + 1
        counter += 1
    elif "C Z" in line:
        total_points += 3 + 3
        counter += 1
    elif "C Y" in line:
        total_points += 0 + 2
        counter += 1
    
print(counter) #muss 2500 sein (debug)
print(total_points)
"""

### PART TWO
total_points_correct = 0 # stores the total points according to the correct plan
three_point_condition = ["C Y", "A X", "B Z"] # I choose Scissors
two_point_condition = ["B Y", "A Z", "C X"] # I choose Paper
one_point_condition = ["A Y", "C Z", "B X"] # I choose Rock
for line in content:
    if "Z" in line:
        total_points_correct += 6
    elif "Y" in line:
        total_points_correct += 3
    else:
        # not necessary
        total_points_correct += 0
    if any(x in line for x in one_point_condition):
        total_points_correct += 1
    elif any(x in line for x in two_point_condition):
        total_points_correct += 2
    elif any(x in line for x in three_point_condition): # or else
        total_points_correct += 3
print(total_points_correct)