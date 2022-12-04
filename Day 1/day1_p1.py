file = open("Day 1/input.txt", 'r')

elfCalories = []
calCount = 0

for line in file:

    if line == '\n':
        elfCalories.append(int(calCount))
        calCount = 0

    elif '\n' not in str(line):
        calCount += int(line)
        elfCalories.append(int(calCount))

    else:
        calCount += int(line)

elfMost = elfCalories[0]
for i in range(len(elfCalories)):

    if elfCalories[i] > elfMost:
        elfMost = elfCalories[i]
    
    else:
        pass

print(elfCalories)
print(elfMost)