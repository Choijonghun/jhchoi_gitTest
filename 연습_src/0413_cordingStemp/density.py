#소금물의 퍼센트 농도와 소금물의 양을 입력하고, end를 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.

#입력에는 소수점 자리수의 제한이 없지만, 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

#입력 횟수는 최대 10회이다.
'''
입력 예1

1% 400g
8% 300g
end
입력 예2

12.245% 21.258g
42.18% 6.826g
0.169% 32.33g
end
출력 예1

4.0% 700.0g
출력 예2

9.16% 60.41g
'''
def density():
  sos = []
  muls = []
  sogum,sogummul = 0,0
  for x in range(10):
    end = input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오\n(end입력 시 종료)\n:")
    if end == "end":
      break
    else:
      a, b = end[:end.find("%")], end[end.find("%")+2:end.find('g')]
      sos.append(float(a) * float(b) / 100)
      muls.append(float(b))
  for so in sos:
    sogum = sogum + so
  for mul in muls:
    sogummul = sogummul + mul
  nong = round(sogum/sogummul*100,2)
  sogummul = round(sogummul,2)
  print(f"농도 : {nong}%\n소금물 : {sogummul}g")

  

  

