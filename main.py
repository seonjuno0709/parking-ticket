import time
from ticket_cal import ticket_calculator

input_hour = input("들어온 시간입력: ")
input_minute = input("들어온 분입력: ")

input_time = int(input_hour)*60 + int(input_minute)

tm = time.localtime()
now_hour = int(tm.tm_hour)
now_min = int(tm.tm_min)
now_time = now_hour*60 + now_min

if 0 <= now_hour < 19: 
    result = now_time - input_time - 60
    ticket_calculator(result)

elif 19<= now_hour < 24:
    # 7시 이후에 들어온 경우
    if 19*60 - input_time < 0:
        result = now_time - input_time - 180
        ticket_calculator(result)

    # 7시 이전에 들어온 경우
    elif 19*60 - input_time >= 0:
        first_time_section = 19*60 - input_time
        second_time_section = now_time - 19*60
        if second_time_section - 180 < 0:
            second_time_section = 0
            result = first_time_section - 60
            ticket_calculator(result)

        elif second_time_section - 180 >= 0:
            second_time_section = second_time_section - 180
            result = first_time_section - 60 + second_time_section
            ticket_calculator(result)
      

