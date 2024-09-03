# 9/3

## 1. 나머지가 1이 되는 수 찾기

# def solution(n):
#     answer = 0
#     for i in range(n-1, 1, -1):
#         if n % i == 1:
#             answer = i
#     return answer

# print(solution(int(input())))


## 2. 음양 더하기

# def solution(absolute, signs):
#     answer = 0
#     for i in range(0, len(signs)):
#         if signs[i] == False:
#             answer = answer + (-1)*absolute[i]
#         else:
#             answer = answer + absolute[i]
#         print(answer)
#         print(absolute[i])
#     return answer

# a=list(map(int, input().split(',')))
# b=list(map(lambda x:x == 'true', input().split(',')))

# print(a,b)
# # print(solution(list(map(int, input().split(','))), list(map(bool, input().split(',')))))

# print(solution(a,b))


## 3. 없는 숫자 더하기

# def solution(numbers):
#     answer = 45
#     for i in numbers:
#         answer -= i
#     return answer


## 4. 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]
    return answer