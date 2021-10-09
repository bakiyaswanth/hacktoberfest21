# function

def BinarySearch(arr, left, right, key):
    
    while left <= right:
        mid = left +(right-1) // 2;

        # check key is present at mid
        if arr[mid] == key:
            return mid

        # if key is greater, ignore left half    
        elif arr[mid] < x:
            left = mid + 1

        # if key is smaller, ignore right half
        else:
            right = mid -1

    # if element was not found
    return -1



# Drived code
arr = [2, 4, 5, 9, 45,1, 6]
key = 5

# function  call
result = BinarySearch(arr, 0, len(arr)-1, key)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")    
