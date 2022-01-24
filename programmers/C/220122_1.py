#1번 : 순차반복
#2번 : 2, 1, 2, 3, 2, 4, 2, 5 반복
#3번 : 3부터 2번씩 순차반복

#시험 10000문제
#리턴 오름차순

def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s1_count = 0
    s2_count = 0
    s3_count = 0

    #반복문을 돌면서 정답과 해당사람의 답이 일치할 때 정답 수를 올려준다
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            s1_count += 1
        if answers[i] == s2[i % len(s2)]:
            s2_count += 1
        if answers[i] == s3[i % len(s3)]:
            s3_count += 1

    #정답 수를 변수에 저장해준다
    answer_temp = [s1_count, s2_count, s3_count]

    # 가장 많이 맞춘 사람 보여주기
    # 역시 반복문을 돌면서 점수를 체크해서 그 사람에게 점수를 더해준다
    for i, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(i + 1)

    return answer