import heapq   # 우선순위 큐를 사용하기 위한 라이브러리

food_times = list(map(int, input().split()))
k = int(input())


def solution(food_times, k):
    hq = []
    fnum = len(food_times)   # 남은 음식의 개수
    answer = 0

    # 시간이 적게 걸리는 음식부터 빼야 하기 때문에 우선순위 큐 사용
    for i in range(fnum):
        heapq.heappush(hq, (food_times[i], i+1))

    previous = 0   # 이전에 제거한 음식의 food_time

    while hq:
        # 음식을 먹는데 걸리는 총 시간 = 남은 시간 * 남은 음식 개수
        time = (hq[0][0]-previous) * fnum

        # 시간이 남을 경우에는 우선순위 큐에서 현재 음식 빼기 (다먹음)
        if k >= time:
            k -= time   # 전체 시간에서 빼기
            previous = heapq.heappop(hq)[0]   # 이전 음식의 food_time 재설정
            fnum -= 1   # 다 먹은 음식 빼기
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % fnum
            hq.sort(key=lambda x: x[1])   # 번호 순으로 먹기 때문에 번호 순으로 정렬
            answer = hq[idx][1]   # 다시 먹어야 할 음식의 번호 출력
            break

    return answer


print(solution(food_times, k))
