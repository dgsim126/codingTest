def solution(players, callings):
    answer = []
    for i in range(len(callings)):
        index = 0
        for j in range(len(players)):
            if players[j] == callings[i]:
                index = j
                break
        players.pop(index)
        player = callings[i]
        players.insert(index-1, callings[i])
    answer = players
    return answer