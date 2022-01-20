import re

def solution(phone_number):
    if len(phone_number)>=4 and len(phone_number)<=20 :
        answer = re.sub('[0-9]','*', phone_number[:-4])
        answer = answer+phone_number[-4:]
        return answer
    else :
        print('전화번호를 정확히 입력해주세요.')

solution('01056103219')