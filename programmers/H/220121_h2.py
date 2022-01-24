new_array = []


def solution(arr):
    for i in arr:
        for j in arr:
            if arr[i] != arr[j]:
                new_array.append(arr[j])


# def solution(arr):
#     answer = []
#     if answer
