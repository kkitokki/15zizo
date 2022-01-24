#1번 : 순차반복
#2번 : 2, 1, 2, 3, 2, 4, 2, 5 반복
#3번 : 3부터 2번씩 순차반복

#시험 10000문제
#리턴 오름차순

def solution(answers):
    #정답카운트 리스트를 만들어줌
    counts = [0, 0, 0]
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ]

    #반복문을 돌면서 정답과 해당사람의 답이 일치할 때 정답 수를 올려준다 > 리스트에 저장
    for i in range(len(answers)):
        if answers[i] == s1[(i % 5)]:
            counts[0] += 1
        if answers[i] == s2[(i % 8)]:
            counts[1] += 1
        if answers[i] == s3[(i % 10)]:
            counts[2] += 1

    # 가장 많이 맞춘 사람 보여주기
    # 반복문을 돌면서 맞춘 개수중 최대값 출력
    for i in range(3):
        if counts[i] == max(counts):
            answer.append(i + 1)

    return answer