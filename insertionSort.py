# Function to perform insertion sort
def insertion_sort(arr):
    # Traverse from index 1 to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted at the correct position
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at the correct position
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)

# Call the insertion sort function
insertion_sort(arr)

# Output the sorted array
print("Sorted array:", arr)
