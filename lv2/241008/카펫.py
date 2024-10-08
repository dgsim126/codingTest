def solution(brown, yellow):
    wh_list = []
    answer = []
    for i in range(3, int((brown+yellow)**0.5)+1):
        if (brown + yellow) % i == 0:
            w = i
            h = (brown+yellow)//i
            if w < h:
                w, h = h, w
            wh = [w, h]
            wh_list.append(wh)
    for i in wh_list:
        if brown != ((i[0] * 2) + 2 * (i[1] - 2)) or yellow != ((i[0]-2) * (i[1]-2)):
            continue
        else:
            answer.append(i[0])
            answer.append(i[1])
            break

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))