# 핸드폰 번호 가리기
def solution(phone_number):
    answer = ''

    # 번호길이 정의
    phone_number_len = len(phone_number)

    # (전체길이 - 4) =뒤 4자리 제외하고 *로 대체
    # (-5= 자릿수 하나 사라짐, -6= 자릿수 둘 사라짐)
    # (-3= 자릿수 하나 더 생김, -2= 자릿수 둘 더 생김)
    answer = '*' * (phone_number_len - 4)

    # phone_number 본문 뒤에서부터 4자리 출력
    answer += phone_number[-4:]
    return answer