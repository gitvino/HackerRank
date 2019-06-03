def hourglassSum(arr):
    max = -63
    for row in range(0, len(arr) - 2):
        for col in range(0, len(arr[row]) - 2):
            sum = arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] + arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
           # print(sum, max)
            if (sum > max):
                max = sum
    return max

if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    print(hourglassSum(arr))