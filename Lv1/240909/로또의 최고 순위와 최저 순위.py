def solution(lotto, win_num):
    check= [0]*46
    correct= 0
    possible= 0

    for num in win_num:
        check[num]+=2

    for num in lotto:
        check[num]+=1

    for i in range(1, len(check)):
        if(check[i]==3):
            correct+=1
        elif(check[i]==2):
            possible+=1

    zero= check[0]
    first_correct= correct

    if(zero<=possible):
        correct+=zero
    else:
        correct+=possible

    rankList= [6,6,5,4,3,2,1]

    return [rankList[correct], rankList[first_correct]]

## main ##
lottos= [45, 4, 35, 20, 3, 9]
win_nums= [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))