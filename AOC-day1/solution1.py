# Define the file name
file_name = 'input.txt'

# Initialize arrays for left and right numbers
left_numbers = []
right_numbers = []

total = 0

# Open the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            left_numbers.append(int(parts[0]))
            right_numbers.append(int(parts[1]))

# Print the arrays
print("Left Numbers:", left_numbers)
print("Right Numbers:", right_numbers)

left_numbers.sort()
right_numbers.sort()

# Count occurrences of each number in the right column
for i in range(len(left_numbers)):
    total += left_numbers[i] * right_numbers[i]


# Print the total
print("Total:", total)

