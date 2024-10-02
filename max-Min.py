# Function to find the maximum and minimum using divide and conquer
def find_max_min(arr, low, high):
    # If the list contains only one element
    if low == high:
        return arr[low], arr[low]
    
    # If the list contains two elements
    if high == low + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))
    
    # If there are more than two elements, divide the array into two halves
    mid = (low + high) // 2
    left_min, left_max = find_max_min(arr, low, mid)
    right_min, right_max = find_max_min(arr, mid + 1, high)
    
    # Combine results
    return min(left_min, right_min), max(left_max, right_max)

# Example usage
arr = [100, 34, 56, 78, 89, 21, 9]
low = 0
high = len(arr) - 1

min_value, max_value = find_max_min(arr, low, high)

print(f"Minimum: {min_value}, Maximum: {max_value}")
