import numpy as np


def main():
    numpyArray = np.array([1, 2, 3, 4, 5])
    numpyArray2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    print(numpyArray)
    print(numpyArray2)
    print(numpyArray.dtype)
    print(numpyArray2.dtype)
    print(numpyArray.ndim)
    print(numpyArray2.ndim)
    print(np.shape(numpyArray))
    print(np.shape(numpyArray2))
    print(np.size(numpyArray))
    print(np.size(numpyArray2))
    print(numpyArray2[1, 2])

    # array of range
    np_arr = np.arange(10)
    print(np_arr)

    # array random
    np_arr = np.linspace(10, 20, 4)
    print(np_arr)

    # array random int
    np_arr = np.random.randint(0, 100, 20)
    print(np_arr)

    # array of constants
    np_arr = np.zeros(5)
    print(np_arr)
    np_arr = np.zeros((4, 5))
    print(np_arr)
    np_arr = np.ones(5)
    print(np_arr)
    np_arr = np.ones((4, 5))
    print(np_arr)
    np_arr = np.ones((4, 5), dtype=int)
    print(np_arr)

    # empty, full and fill arrays
    np_arr = np.empty(10, dtype=int)
    np_arr.fill(9)
    print(np_arr)
    np_arr = np.full(5, 10)
    print(np_arr)
    np_arr = np.full((3, 2), 7)
    print(np_arr)

    # add or remove elements in array
    np_arr = np.array([1, 2, 3, 5])
    np_arr = np.insert(np_arr, 3, 4)
    print(np_arr)
    np_arr = np.append(np_arr, 6)
    print(np_arr)
    np_arr = np.delete(np_arr, 3)
    print(np_arr)

    # sorted array
    np_arr = np.random.randint(0, 20, 20)
    print(np_arr)
    np_arr = np.sort(np_arr)
    print(np_arr)
    np_arr = np.array([[8, 3, 5, 2], [4, 3, 2, 1]])
    print(np_arr)
    np_arr = np.sort(np_arr)
    print(np_arr)

    # assignment var1 = var 2 means they both use the same memory/address, use copy to get a copy.
    # Use .base (= None if array owns data or returns the base array)

    # reshape array
    np_arr = np.arange(1, 13)
    print(np_arr)
    np_arr = np.reshape(np_arr, (3, 4))
    print(np_arr)
    np_arr = np.reshape(np_arr, (3, 2, 2))
    print(np_arr)
    np_arr = np.reshape(np_arr, -1)
    print(np_arr)

    # indexing and slicing is the same as python [start:stop before: increment]
    # outs an empty array if increment with start-stop is invalid
    print(np_arr[-3:1:-1])

    # join arrays
    np_arr = np.arange(1, 13)
    np_arr2 = np.arange(1, 4)
    np_arr = np.concatenate((np_arr, np_arr2))
    print(np_arr)
    np_arr = np.array([[1, 2, 3], [9, 8, 7]])
    np_arr2 = np.array([[4, 5], [6, 5]])
    np_arr = np.concatenate((np_arr, np_arr2), axis=1)
    print(np_arr)
    np_arr = np.arange(1, 13)
    np_arr2 = np.arange(11, 23)
    np_arr = np.stack((np_arr, np_arr2))
    print(np_arr)
    np_arr = np.arange(1, 13)
    np_arr2 = np.arange(11, 23)
    np_arr = np.hstack((np_arr, np_arr2))
    print(np_arr)
    np_arr = np.arange(1, 13)
    np_arr2 = np.arange(11, 23)
    np_arr = np.vstack((np_arr, np_arr2))
    print(np_arr)

    # split arrays
    np_arr = np.arange(1, 13)
    np_arr = np.split(np_arr, 4)
    print(np_arr)

    # vector
    np_arr = np.arange(1, 10)
    np_arr2 = np.arange(21, 30)
    np_res = np_arr + np_arr2
    print(np_res)
    np_res = np_arr2 - np_arr
    print(np_res)
    np_res = np_arr * np_arr2
    print(np_res)
    np_res = np_arr / np_arr2
    print(np_res)
    np_res = np_arr ** np_arr2
    print(np_res)
    np_res = np_arr * 2
    print(np_res)
    np_res = np.mod(np_arr, np_arr2)
    print(np_res)
    np_res = np.sqrt(np_arr)
    print(np_res)
    np_res = np.power(np_arr, np_arr2)
    print(np_res)

    # broadcasting
    np_arr = np.arange(1, 10).reshape(3, 3)
    np_arr2 = np.arange(1, 4)
    np_res = np_arr + np_arr2
    print(np_res)

    # agg functions
    np_arr = np.arange(1, 10).reshape(3, 3)
    np_arr2 = np.arange(1, 4)
    np_res = np_arr.sum()
    print(np_res)
    np_res = np_arr2.sum()
    print(np_res)
    np_res = np_arr.sum(axis=0)
    print(np_res)
    np_res = np_arr.sum(axis=1)
    print(np_res)
    np_res = np_arr.prod()
    print(np_res)
    np_res = np_arr.prod(axis=0)
    print(np_res)
    np_res = np_arr.prod(axis=1)
    print(np_res)
    np_res = np.average(np_arr)
    print(np_res)
    np_res = np.average(np_arr2)
    print(np_res)
    np_res = np.max(np_arr)
    print(np_res)
    np_res = np.min(np_arr2)
    print(np_res)
    np_res = np.mean(np_arr)
    print(np_res)
    np_res = np.std(np_arr)
    print(np_res)

    # unique values and count
    np_arr = np.array([1,2,3,5,2,4,23,54,32,2,4,6,7,4,65,7,4,6,4,3,6,3,6])
    np_arr2 = np.array([[1, 2, 3, 1], [2, 4, 6, 2], [1, 2, 3, 1], [3, 5, 7, 3]])
    np_res = np.unique(np_arr)
    print(np_res)
    np_res = np.unique(np_arr2)
    print(np_res)
    np_res = np.unique(np_arr2, axis=0)
    print(np_res)
    np_res = np.unique(np_arr2, axis=1)
    print(np_res)
    np_res = np.unique(np_arr, return_index=True)
    print(np_res)
    np_res = np.unique(np_arr, return_counts=True)
    print(np_res)

    # transpose operations
    np_arr = np.arange(12).reshape(3, 4)
    np_arr2 = np.arange(6).reshape(3, 2)
    np_arr3 = np.arange(24).reshape(2, 3, 4)
    np_res = np.transpose(np_arr)
    print(np_res)
    np_res = np.transpose(np_arr2)
    print(np_res)
    np_res = np.moveaxis(np_arr3, 0, -1)
    print(np_res)
    np_res = np.swapaxes(np_arr3, 0, 2)
    print(np_res)

    # reversing
    np_arr = np.arange(12)
    np_arr2 = np.arange(12).reshape(3, 4)
    np_arr3 = np.arange(24).reshape(2, 3, 4)
    np_res = np_arr[::-1]
    print(np_res)
    np_res = np.flip(np_arr)
    print(np_res)
    np_res = np_arr2[::-1]
    print(np_res)
    np_res = np.flip(np_arr2)
    print(np_res)
    np_res = np.flip(np_arr3, axis=1)
    print(np_res)
    np_res = np.flip(np_arr3, axis=0)
    print(np_res)
    np_res = np.flip(np_arr3, axis=2)
    print(np_res)
    

if __name__ == '__main__':

    main()


