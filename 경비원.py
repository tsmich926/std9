def get_distance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

# 입력
w, h = map(int, input().split()) #총 가로세로 길이 입력
n = int(input()) #상점 개수 입력

course = []
for _ in range(n + 1):  # 북쪽 (0) 에서 상점까지의 거리
    x, y = map(int, input().split())
    course.append(get_distance(x, y))

answer = 0
for i in range(n):  # 동근이와 상점 사이의 최단거리
    in_course = abs(course[-1] - course[i]) #정방향으로 거리를 구할때의 거리차를 구한다.
    out_course = 2 * (w + h) - in_course #반대로 거리를 구할때의 거리차를 구한다.
    answer += min(in_course, out_course) # 그 두개중 작은 값을 더해준다.

print(answer)