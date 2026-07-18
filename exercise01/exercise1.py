# Write your solution to exercise 1 here

strings = []

# Collect input until an empty string is provided
while True:
    user_input = input("Type in a string: ")
    if user_input == "":
        break
    strings.append(user_input)

# Calculate the required information
total_strings = len(strings)

# Find the length of the longest string
longest_length = 0
for s in strings:
    if len(s) > longest_length:
        longest_length = len(s)

# Combine all strings to find the most common character
all_chars = "".join(strings)
most_common_char = ""
highest_count = 0

# Count occurrences of each character
for char in set(all_chars):
    count = all_chars.count(char)
    if count > highest_count:
        highest_count = count
        most_common_char = char

# Print the final output
print(f"Total number of strings: {total_strings}")
print(f"The length of the longest string: {longest_length}")
print(f"The most common character in strings: {most_common_char}")
