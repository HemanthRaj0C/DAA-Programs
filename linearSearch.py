# Function to perform linear search
def linear_search(arr, target):
    # Traverse through the array
    for i in range(len(arr)):
        # Check if the current element is the target
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [10, 23, 45, 70, 11, 15]
target = 70

# Call linear search function
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
