from msilib import datasizemask
import time

input_hour = input("시간입력: ")
input_minute = input("분입력: ")

tm = time.localtime()
now_hour = tm.tm_hour

if 19 <= now_hour < 24:
    # 오후 7시부터는 3시간 무료
    input_time = int(input_hour)*60 + int(input_minute) - 60
    if input_time < 0:
        print("시간 등록할 필요가 없습니다")
    else:
        count_time = input_time//30
        print(f"등록할 시간권은 {count_time}개 입니다.")

elif now_hour < 19:
    # 오후 7시전에는 1시간 무료
    input_time = int(input_hour)*60 + int(input_minute) - 60
    if input_time < 0:
        print("시간 등록할 필요가 없습니다")
    else:
        count_time = input_time//30
        print(f"등록할 시간권은 {count_time}개 입니다.")

#문제해결하기
#오후6시에 들어온 사람과 오후7시에 들어온 사람은 계산하는법이 다르다?\
