def solution(array):
    answer = []
    answer.append(array[0])
    #배열의 첫번째 값을 먼저 넣어줌

    for i in range(1, len(array)):
        if array[i - 1] != array[i]:
            answer.append(array[i])
    #이전값과 해당값이 같지않을 때만 배열에 추가해준다

    return answer