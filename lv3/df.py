from datetime import datetime

class TimeSlot:
    def __init__(self, user, start, end):
        self.user = user
        self.start = datetime.strptime(start, '%Y-%m-%d %H:%M')
        self.end = datetime.strptime(end, '%Y-%m-%d %H:%M')

def find_available_times(time_slots):
    # 모든 시작 및 종료 시간 추출
    time_points = set()
    for slot in time_slots:
        time_points.add(slot.start)
        time_points.add(slot.end)

    # 시간 순서대로 정렬
    sorted_time_points = sorted(time_points)

    # 가능한 모든 시간 범위 생성
    available_times = []
    for i in range(len(sorted_time_points) - 1):
        start = sorted_time_points[i]
        end = sorted_time_points[i + 1]
        users_available = []

        # 각 사용자에 대해 해당 시간 범위에 가능한지 확인
        for slot in time_slots:
            if slot.start <= start and slot.end >= end:
                users_available.append(slot.user)

        if users_available:
            available_times.append([start.strftime('%Y-%m-%d %H:%M'), end.strftime('%Y-%m-%d %H:%M'), users_available])

    # 가능한 사용자 수에 따라 정렬
    available_times.sort(key=lambda x: -len(x[2]))

    return available_times

# 입력 데이터 생성
input_data = [
    ['user1', '2024-10-01 14:00', '2024-10-01 15:00'],
    ['user1', '2024-10-03 12:00', '2024-10-03 15:00'],
    ['user1', '2024-10-04 12:00', '2024-10-04 15:00'],
    ['user2', '2024-10-04 12:00', '2024-10-04 14:00'],
    ['user2', '2024-10-04 17:00', '2024-10-04 20:00'],
    ['user3', '2024-10-01 13:00', '2024-10-01 19:00'],
    ['user3', '2024-10-02 10:00', '2024-10-02 12:00'],
    ['user3', '2024-10-04 11:00', '2024-10-04 17:00'],
    ['user4', '2024-10-01 12:00', '2024-10-01 15:00'],
    ['user4', '2024-10-02 17:00', '2024-10-02 20:00'],
    ['user4', '2024-10-03 14:00', '2024-10-03 17:00'],
    ['user4', '2024-10-04 10:00', '2024-10-04 15:00']
]

# TimeSlot 객체 생성
time_slots = [TimeSlot(user, start, end) for user, start, end in input_data]

# 실행
result = find_available_times(time_slots)

# 결과 출력
for period in result:
    print(period)
