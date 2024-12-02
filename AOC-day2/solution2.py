file_name = 'input.txt'


numbers=[]
# Open the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        # Split the line into parts
        parts = line.strip().split()
        # trun all numers in it to integers and split them to seperate arrays in array
        parts = [int(part) for part in parts]
        numbers.append(parts)

def is_safe(report):
    # Check if all levels are either increasing or decreasing with a valid difference between adjacent levels
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        
        # Check if the difference is between 1 and 3
        if diff < 1 or diff > 3:
            return False
        
        # Check if the sequence is strictly increasing or decreasing
        if report[i+1] < report[i]:
            increasing = False
        if report[i+1] > report[i]:
            decreasing = False
    
    # The report is valid if it's either increasing or decreasing
    return increasing or decreasing


total = 0

for sublist in numbers:
    # Check if the report is already safe
    if is_safe(sublist):
        total += 1
        continue
    
    # If not safe, check if removing one element makes it safe
    for i in range(len(sublist)):
        new_sublist = sublist[:i] + sublist[i+1:]
        if is_safe(new_sublist):
            total += 1
            break 


print(total)
