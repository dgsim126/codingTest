# 테스트 케이스 3번 실패(87.5%)
# 입출력 예제 출력의 4번째 len이 4라 앞에 공백이면 제거하는 코드 작성했지만 실패(뭐가 문제인지 모르겠음)

def solution(n, arr1, arr2):
    sol1 = toTwo(arr1, n)
    sol2 = toTwo(arr2, n)
    result= [""]*n

    print(sol1)
    print(sol2)

    for i in range(n):
        for j in range(n):
            if(sol1[i][j]==1 or sol2[i][j]==1):
                result[i]+="#"
            else:
                result[i]+=" "

    return result


def toTwo(arr, n):
    result = [[0 for i in range(n)] for j in range(n)]  # 2차원 배열 만들기

    for i in range(len(arr)):  # 입력받은 값을 하나씩 꺼냄
        flag = n - 1
        while (arr[i] >= 2):
            result[i][flag] = arr[i] % 2
            arr[i] //= 2
            flag -= 1
        result[i][flag] = 1

    return result


## main ##
n = 5
arr1 = 	[9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))