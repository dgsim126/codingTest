# dfs로 모든 경우를 순회
# dfs의 결과 [1, 3, 0, 2]와 같이 중복되는 수가 없고, 바로 옆에 있는 숫자가 1차이가 아닌 모든 경우가 정답

def solution(n):
    global cnt
    cnt= 0

    is_used= [0]*n
    result= [-1]*n

    dfs(0, is_used, result, n)

    return cnt


def dfs(depth, is_used, result, n):
    global cnt

    # 탈출 조건
    if(depth==n):
        cnt+=1
        return cnt

    for i in range(n):
        if(is_used[i]==0):
            if(depth==0):
                is_used[i]= 1
                result[depth]= i

                dfs(depth+1, is_used, result, n)

                is_used[i]= 0
                result[depth] = -1
            else:
                if(abs(i-result[depth-1])==1):
                    is_used[i]= 1
                    result[depth]= i

                    dfs(depth+1, is_used, result, n)

                    is_used[i]= 0
                    result[depth]= -1

## main ##
n= 4
print(solution(n))