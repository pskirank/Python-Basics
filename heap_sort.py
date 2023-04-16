def heapsort(arr):
    def sift_down(arr, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child+1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    #Max Heap building
    for start in range((len(arr)-2)//2, -1, -1):
        sift_down(arr, start, len(arr)-1)
    #Heap sort
    for end in range(len(arr)-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end-1)
    return arr

if __name__ == '__main__':
    arr = list(map(int, input("Enter the Array of elements with spaces between them:").split()))
    print("Sorted array after heapification:", heapsort(arr))
