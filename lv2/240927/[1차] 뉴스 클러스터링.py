def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str1_list = []
    str2 = str2.upper()
    str2_list = []
    dic = {
        "A" : 1,
        "B" : 2,
        "C" : 1,
        "D" : 2,
        "E" : 1,
        "F" : 2,
        "G" : 1,
        "H" : 2,
        "I" : 1,
        "J" : 2,
        "K" : 1,
        "L" : 2,
        "M" : 1,
        "N" : 2,
        "O" : 1,
        "P" : 2,
        "Q" : 1,
        "R" : 2,
        "S" : 1,
        "T" : 2,
        "U" : 1,
        "V" : 2,
        "W" : 1,
        "X" : 2,
        "Y" : 1,
        "Z" : 2
    }
    
    for i in range(len(str1)-1):
        if str1[i] not in dic or str1[i+1] not in dic:
            continue
        else:
            str1_list.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i] not in dic or str2[i+1] not in dic:
            continue
        else:
            str2_list.append(str2[i]+str2[i+1])
    
    if str2_list == [] and str1_list == []:
        return 65536
    
    dic2 = {}
    dic3 = {}
    for i in range(len(list(set(str1_list)))):
        dic2[list(set(str1_list))[i]] = 0
        dic3[list(set(str1_list))[i]] = 0
    for i in range(len(list(set(str2_list)))):
        dic3[list(set(str2_list))[i]] = 0
        dic2[list(set(str2_list))[i]] = 0
    for i in range(len(str1_list)):
        dic2[str1_list[i]] = dic2[str1_list[i]] + 1
    for i in range(len(str2_list)):
        dic3[str2_list[i]] = dic3[str2_list[i]] + 1
    
    str1_list = list(set(str1_list))
    str2_list = list(set(str2_list))

    union = 0
    intersection = 0
    for i in range(len(list(set((str1_list+str2_list))))):
        union += max(dic2[list(set((str1_list+str2_list)))[i]], dic3[list(set((str1_list+str2_list)))[i]])
        intersection += min(dic2[list(set((str1_list+str2_list)))[i]], dic3[list(set((str1_list+str2_list)))[i]])
    
    answer = int((intersection / union) * 65536)
    
    return answer

print(solution("FRANCE", "french"))
# print(solution("handshake", "shake hands"))
# print(solution("E=M*C^2","e=m*c^2"))
# print(solution("aa1+aa2", "AAAA12"))