# 1. Create a list of even numbers from 2 to 20
numbers = list(range(2, 21, 2))

# 2. Append 22 to the list
numbers.append(22)

# 3. Remove the smallest number (2)
numbers.pop(0)   # removes the first element

# 4. Compute sum and average
total_sum = sum(numbers)
average = total_sum / len(numbers)

# 5. Print results
print(f"Numbers: {numbers}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
