# Define the file name
file_name = 'input.txt'

# Initialize arrays for left and right numbers
left_numbers = []
right_numbers = []
hash_map = {}
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

# Count occurrences of each number in the right column
for number in right_numbers:
    if number in hash_map:
        hash_map[number] += 1
    else:
        hash_map[number] = 1

# Calculate the total
for number in left_numbers:
    if number in hash_map:
        total += number * hash_map[number]

print("Total:", total)
