def ticket_calculator(result):
  if result < 0:
    print("주차권을 등록할 필요가 없습니다.")
  elif result == 0:
    print(f"필요한 주차권의 개수는 1개 입니다.")
  else:
    ticket_count = result//30 + 1
    print(f"필요한 주차권의 개수는 {ticket_count}개 입니다.")