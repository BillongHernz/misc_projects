
def selection_sort(in_arr):
    # Traverse through all array elements
    for i in range(len(in_arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(in_arr)):
            if in_arr[min_idx] > in_arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        in_arr[i], in_arr[min_idx] = in_arr[min_idx], in_arr[i]


if __name__ == '__main__':
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    selection_sort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" ")

    arr = [1,2,3,4,5,6,7,8,9,10]

    selection_sort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" ")
