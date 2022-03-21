
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    # Driver code to test above
    in_arr = [64, 34, 25, 12, 22, 11, 90]

    mergeSort(in_arr)

    print("Sorted array is:")
    for i in range(len(in_arr)):
        print("% d" % in_arr[i], end=" ")

    in_arr = [1,2,3,4,5,6,7,8,9,10]

    mergeSort(in_arr)

    print("Sorted array is:")
    for i in range(len(in_arr)):
        print("% d" % in_arr[i], end=" ")