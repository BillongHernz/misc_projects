
def bubble_sort(in_arr):
    n = len(arr)

    for i in range(n - 1):
        print(i)
        no_swap = True
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swap = False
        if no_swap:
            break


if __name__ == '__main__':
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" \n")

    arr = [1,2,3,4,5,6,7,8,9,10]

    bubble_sort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" \n")
