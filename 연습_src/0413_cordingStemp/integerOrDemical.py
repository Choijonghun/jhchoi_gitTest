#프로그래머 X는 입력값을 숫자를 입력하거나 문자를 입력하려고 하는데,

#만약 숫자를 입력하였으면 그것이 정수인지, 소수인지 구별하는 프로그램을 짜보도록 하고,
#만약 문자를 입력하였으면 숫자가 아니므로 math error를 표시하게 하라

def gubun():
  try:
    x = input("숫자를 입력하시오 \n:")
    x = float(x)
    if x - int(x) == 0:
      print(f"[{x}]는 정수 입니다.")
    elif x - int(x) != 0:
      print(f"[{x}]는 소수 입니다.")

  except ValueError:
    print("math error")