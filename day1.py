f = open("input_day1.txt", "r")
### PART ONE
highest_calorie = 0 # to save the "current" highest calorie
content = f.readlines()

tmp = 0 # tmp to store temporary potential highest calorie value
for line in content:
    # Debug
    # print("line: ",line)
    if line !="\n":
        # if the line is not a new line, it adds the integer value to the temporary variable
        tmp += int(line)
    else:
        # if the line is a "new line" it compares the temporary value with the current highest calorie 
        if tmp > highest_calorie:
            highest_calorie = tmp
            # Debug
            # print("Tmp: ",tmp)
        # resets temporary value
        tmp = 0

print("The Elf carrying the most Calories, is carrying",highest_calorie,"Calories")

### PART TWO
#creates a list instead
highest_calorie_list = []
tmp = 0
for line in content:
    # Debug
    # print("line: ",line)
    if line !="\n":
        # if the line is not a new line, it adds the integer value to the temporary variable
        tmp += int(line)
    else:
        # if the line is a "new line" it adds the new calorie value of that elf to the list
        highest_calorie_list.append(tmp)
        # resets temporary value
        tmp = 0

highest_calorie_list.sort(reverse=True)
total_highest_calorie = highest_calorie_list[0] + highest_calorie_list[1] + highest_calorie_list[2]
# DEBUG
# print(highest_calorie_list[:3])
print("The top three Elfs carrying with the most Calories, are carrying",total_highest_calorie,"Calories")

f.close()