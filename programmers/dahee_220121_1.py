# 함수작성
def solution(answers):
    solve1 = []
    solve2 = []
    solve3 = []
    length = len(answers)

    # solve1 / 1번 수포자가 찍는 방식
    for i in range(length):
        solve1.append(i % 5 + 1)

    # solve2 / 2번 수포자가 찍는 방식
    j = 0
    for i in range(length):
        if i % 2 == 0:
            solve2.append(2)
        else:
            solve2.append(j % 5 + 1)
            if j % 5 == 0:
                j += 2
            else:
                j += 1

    # solve3 / 3번 수포자가 찍는 방식
    list_int = length // 10
    list_num = length % 10
    list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    solve3 = list * list_int
    for i in list[:list_num]:
        solve3.append(i)
    # 지역변수선언
    answer = []
    correct_answer = []
    ox1 = []
    ox2 = []
    ox3 = []

    if length <= 10000:
        for i in range(length):
            if solve1[i] == answers[i]:
                ox1.append('1')
            else :
                ox1.append('0')

            if solve2[i] == answers[i]:
                ox2.append('1')
            else :
                ox2.append('0')

            if solve3[i] == answers[i]:
                ox3.append('1')
            else :
                ox3.append('0')

        a = ox1.count('1')
        b = ox2.count('1')
        c = ox3.count('1')
        correct_answer.append(a)
        correct_answer.append(b)
        correct_answer.append(c)
        print(correct_answer)

        max_score = max(correct_answer)
        for i in range(len(correct_answer)):
            if correct_answer[i] == max_score:
                answer.append(i+1)
        print(answer)
        return answer

answers = [1,2,3,4,5]
solution(answers)

