def solution(phone_number):
    #길이만큼 *로 변환
    #나머지 부분은 그대로 붙여서 answer에 저장
    answer= "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer

#출력
print("전화번호를 -제외하고 숫자만 입력해주세요.")
phone_number = input("전화번호:",)
print(solution(phone_number))