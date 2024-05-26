def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        
        # If the target is found at the middle
        if arr[mid] == target:
            return mid
        
        # If the target is smaller than the middle element, search in the left subarray
        elif arr[mid] > target:
            return mid, binary_search(arr, low, mid - 1, target)
        
        # If the target is larger than the middle element, search in the right subarray
        else:
            return mid, binary_search(arr, mid + 1, high, target)
    else:
        # If the element is not present in the array
        return None

def draw_recursive_calls(arr, low, high, level=0):
    mid = (low + high) // 2
    print("  " * level, f"({low}, {high}) - {arr[mid]}")
    
    if low <= high:
        draw_recursive_calls(arr, low, mid - 1, level + 1)
        draw_recursive_calls(arr, mid + 1, high, level + 1)

if name == "main":
    arr = [10, 35, 40, 45, 50, 55, 60, 65, 70, 100]
    target = 100
    
    print("Array:", arr)
    print("Target:", target)
    
    index, tree = binary_search(arr, 0, len(arr) - 1, target)
    
    if index is not None:
        print(f"Element {target} is present at index {index}")
    else:
        print(f"Element {target} is not present in the array")
    
    print("\nRecursive calls:")
    draw_recursive_calls(arr, 0, len(arr) - 1)
