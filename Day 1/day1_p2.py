file = open("Day 1/input.txt", 'r')

elfCalories = []
calCount = 0
elfMost = 0

for line in file:

    if line == '\n':
        elfCalories.append(int(calCount))
        calCount = 0

    elif '\n' not in str(line):
        calCount += int(line)
        elfCalories.append(int(calCount))

    else:
        calCount += int(line)

elfCalories.sort(reverse=True)

for i in range(0,3):
    elfMost += elfCalories[i]

print(elfMost)