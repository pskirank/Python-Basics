import os
# Complete the hourglassSum function below.


def hourglass_sum(arr):
    list1 = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            list1.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]
                         + arr[i+2][j+2])
    return max(list1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglass_sum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()