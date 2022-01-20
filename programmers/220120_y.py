def solution(phone_number):
    answer= "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer

print("전화번호를 -제외하고 숫자만 입력해주세요.")
phone_number = input("전화번호:",)
print(solution(phone_number))