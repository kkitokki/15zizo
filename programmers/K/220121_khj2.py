def solution(arr):
    # 배열 정의
    answer = []
    # 하나씩
    for i in range(len(arr)):
        # 첫 인덱스 = 입력
        if i == 0:
            answer.append(arr[i])
        # i > 1일 때 이 전과 원소 다를 때 입력
        if i >= 1:

            if arr[i - 1] != arr[i]:
                answer.append(arr[i])

    return answer

# 처음=예외처리, 이전 인덱스 원소가 다를 때 답안 리스트에 들어가게 함.