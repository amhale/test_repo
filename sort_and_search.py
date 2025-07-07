#establish list
list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

#print original list
print("Original list:", list)

#sort list using insertion sort
def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

#sort list
insertion_sort(list)
#print sorted list
print("Sorted list:", list)

#define binary search function
def binary_search(target, items):
    low, high = 0, len(items) - 1
    
    while high >= low: # Keep iterating until the low and high cross
        # Find midpoint
        mid = (low + high) // 2
         # If item is found at midpoint, return its index
        if items[mid] == target:
            return mid
        # Else, if item at midpoint is less than target,
        # search the second half of the list
        elif items[mid] < target:
            low = mid + 1
        # Else, search the first half
        else:
            high = mid - 1
    # Returns None if item not found
    return None 

#use binary search function to find index of 9
index = binary_search(9, list)
#check if index is not None
if index is not None:
    print(f"Number 9 found at index: {index}")
else:
    print("Number 9 not found in the list")

#I think that the binary search is the best option as it works quickly to search a list and is efficient for large lists.
#However, it requires the list to be sorted beforehand.

