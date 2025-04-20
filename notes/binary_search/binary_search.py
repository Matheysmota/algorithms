def binary_search(array, item, right=0, left=None):
    if left is None:
        left = len(array)-1
     
    if right <= left:
        mid =  (right + left)//2
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            return binary_search(array, item, right, mid - 1)
        else:
            return binary_search(array, item, mid + 1, left)
        
    return None     