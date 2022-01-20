def solution(phone_number):
    secret_number = ''
    last_number = phone_number[-4:]
    for number in phone_number[0:-4]:
        number = '*'
        secret_number += number
    return secret_number + last_number
