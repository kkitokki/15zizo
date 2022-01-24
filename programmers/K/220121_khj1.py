# enumerate, 완전탐색

def solution(answers):
    # 찍는방식 정의
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 맞힌 갯수 정의
    count_a, count_b, count_c = 0, 0, 0
    answer = []

    # 정답 수만큼 for문
    for i in range(0, len(answers)):

        # 찍는 방식의 문제번호가 갯수 넘었을때 회귀, 찍기 갯수만큼 나누고 나머지 찾기
        if answers[i] == a[i % len(a)]:
            count_a += 1
        if answers[i] == b[i % len(b)]:
            count_b += 1
        if answers[i] == c[i % len(c)]:
            count_c += 1

    max_count = max(count_a, count_b, count_c)
    # 최다정답자? = if문. 동점자 분류 위해 3번 반복
    if max_count == count_a:
        answer.append(1)
    if max_count == count_b:
        answer.append(2)
    if max_count == count_c:
        answer.append(3)

    return answer