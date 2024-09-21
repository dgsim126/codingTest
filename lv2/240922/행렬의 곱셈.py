def solution(arr1, arr2):
    answer = [[[0] * len(arr2[0])] * len(arr1)]
    matrix_arr = [[[]] * len(arr2)] * len(arr1)
    print(matrix_arr[0][0])
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            matrix_arr[i][j].append(arr1[i])
    return answer

solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])