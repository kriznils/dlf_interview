f = open("input_day3.txt", "r")
### PART ONE
content = f.readlines()
temp_list = [] # temporary list for better processing
first_compartment = [] # list for fist compartment
second_compartment = [] # list for second compartment
sum_of_priorities = 0 # sum of all item priorities that are in the wrong department
for line in content:
    temp_list = list(line) # list for better processing
    temp_list.pop(-1) # to remove the last item of each list (the "new line")
    first_compartment = temp_list[:len(temp_list)//2]
    second_compartment = temp_list[len(temp_list)//2:]
    print(first_compartment) # Debug to know that the splitting is correct
    print(second_compartment)
    for i in first_compartment:
        if any(x in i for x in second_compartment): # chechs if the current item of the first compartment is also in the second compartment
            print("double: ",i) # DEBUG to know which item is wrong
            if i.islower():
                sum_of_priorities += ord(i) - 96 # using the unicode as reference for lowercase
            else: # isupper
                sum_of_priorities += ord(i) - 38 # using the unicode as reference for lowercase
            break # break after the item is found, because only one item is wrong

print(sum_of_priorities)

### PART TWO
print(len(content))
rucksack_one = [] # every rucksack of the first elve of each group (matrix)
rucksack_two = [] # every rucksack of the second elve of each group (matrix)
rucksack_three = [] # every rucksack of the third elve of each group (matrix)
sum_of_badges = 0
for line in content[::3]: # every third row starting from row 1 (id=0) is the rucksack of the first elve of each group
    temp_list = list(line) # list for better processing
    temp_list.pop(-1) # to remove the last item of each list (the "new line")
    rucksack_one.append(temp_list)
for line in content[1::3]: # every third row starting from row 2 (id=1) is the rucksack of the second elve of each group
    temp_list = list(line) # list for better processing
    temp_list.pop(-1) # to remove the last item of each list (the "new line")
    rucksack_two.append(temp_list)
for line in content[2::3]: # every third row starting from row 3 (id=2) is the rucksack of the third elve of each group
    temp_list = list(line) # list for better processing
    temp_list.pop(-1) # to remove the last item of each list (the "new line")
    rucksack_three.append(temp_list)


group_no = 0 # to point to the correct group number
for i in rucksack_one: # iterates through each "first member"
    for j in i: # iterates through the itams of the rucksack of the first member
        if any(x in j for x in rucksack_two[group_no]) and any(x in j for x in rucksack_three[group_no]): #checks if the item is in both of the other rucksacks of the other members of the group
            if j.islower():
                sum_of_badges += ord(j) - 96 # using the unicode as reference for lowercase
            else: # isupper
                sum_of_badges += ord(j) - 38 # using the unicode as reference for lowercase
            break # break after the badge is found, because only one item is wrong
    group_no +=1 # counter
print(sum_of_badges)