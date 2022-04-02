"""
2020년 카카오 신입 공채 문제
https://programmers.co.kr/learn/courses/30/lessons/60057
"""

s = input()   # 알파벳 소문자로만 이루어진 문자열


def solution(s):
    answer = 0
    length = len(s)   # 문자열의 길이
    result_arr = []   # 각 step마다 나온 문자열의 길이를 담을 배열
    for i in range(1, (length//2 + 1)):   # 예를 들어, 길이가 총 12이면 6덩어리까지 나눌 수 있음.
        temp = ""   # 결과 문자열
        first = s[0:i]
        count = 1
        for j in range(i, length, i):   # 탐색을 덩어리 수만큼
            if first == s[j:j+i]:   # 이전 문자열과 같으면
                count += 1   # count 추가
            else:   # 이전 문자열과 다르면
                # 이전의 문자열을 계산해서 넣어줌
                temp += str(count) + first if count >= 2 else first
                first = s[j:j+i]   # 현재 문자열로 초기화
                count = 1   # count 초기화
        # 끝에 남은 문자열 추가로 넣어줌
        temp += str(count) + first if count >= 2 else first
        result_arr.append(len(temp))   # 문자열 길이 배열에 해당 문자열의 길이 push

    answer = min(result_arr)   # 배열에서 최소값 return
    return answer


print(solution(s))
