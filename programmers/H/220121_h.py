import random

answer = []  # 정답
for number in range(100):
    number = random.randint(1, 5)  # 1~5까지의 랜덤 숫자를 number에 넣는다.
    answer.append(number)  # answer리스트에 100번 추가

give_up_person1 = [1, 2, 3, 4, 5]  # 수포자 1
for number in range(95):  # 위 인덱스 5개를 미리 추가해줬기 떄문에 95번 돌려야 100개가 된다.
    # give_person1의 인덱스를 차례대로 95번 추가
    give_up_person1.append(give_up_person1[number])


give_up_person2 = [2, 1, 2, 2, 2, 3, 2, 4, 2, 5]  # 수포자 2
for number in range(90):  # 위에 인덱스가 이미 10개가 있기 떄문에 100개를 맞추기위해서 range를 90개로 설정
    # give_person2의 인덱스를 차례대로 추가
    give_up_person2.append(give_up_person2[number])

give_up_person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 3
for number in range(90):
    give_up_person3.append(give_up_person3[number])


def solution():
    give_up_answer_count1 = 0  # 각 수포자의 정답 개수
    give_up_answer_count2 = 0
    give_up_answer_count3 = 0
    for number in range(100):
        # 정답과 비교하여 정답개수를 하나씩 증가시킨다.
        if give_up_person1[number] == answer[number]:
            give_up_answer_count1 += 1
        elif give_up_person2[number] == answer[number]:
            give_up_answer_count2 += 1
        elif give_up_person3[number] == answer[number]:
            give_up_answer_count3 += 1
    print(f'수포자 1은 {give_up_answer_count1}문제 맞혔습니다')
    print(f'수포자 2은 {give_up_answer_count2}문제 맞혔습니다')
    print(f'수포자 3은 {give_up_answer_count3}문제 맞혔습니다')

    if give_up_answer_count1 > give_up_answer_count2 and give_up_answer_count1 > give_up_answer_count3:
        print('따라서 가장 문제를 많이 맞힌 사람은 수포자 1 입니다.')
    elif give_up_answer_count2 > give_up_answer_count1 and give_up_answer_count2 > give_up_answer_count3:
        print('따라서 가장 문제를 많이 맞힌 사람은 수포자 2 입니다.')
    elif give_up_answer_count3 > give_up_answer_count1 and give_up_answer_count3 > give_up_answer_count3:
        print('따라서 가장 문제를 많이 맞힌 사람은 수포자 3 입니다.')


solution()
