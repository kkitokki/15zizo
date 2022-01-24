def solution(arr):

    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(arr) <= 1000000 :
        for num in arr :
            if num>=0 and num<=9 :
                for i in range(len(arr)):
                    if i==0:
                        answer.append(arr[0])
                    else:
                        if arr[i] != arr[i-1]:
                            answer.append(arr[i])
                return answer


arr = [1,1,3,3,0,1,1,1]
solution(arr)