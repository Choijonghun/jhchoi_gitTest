class caculation:
  def __init__(self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

  def sub(self, num):
    self.result -= num
    return self.result
  
  def mul(self, num):
    self.result *= num
    return self.result

  def div(self, num):
    self.result /= num
    return self.result

def cacul(b): #계산
  if x in no_oper:
    print("결과 :", math.add(b))
  elif x == "+":
    print("결과 :", math.add(b))
  elif x == "-": 
    print("결과 :", math.sub(b))
  elif x == "*":  
    print("결과 :", math.mul(b))
  elif x == "/":  
    print("결과 :", math.div(b))

math = caculation()
no_oper = ["",0,"\n","0"] #입력하면 종료 되는 값
i = 1

print("계산기 시작 (null 입력시 종료)")
a = int(input("1번째 정수를 입력하세요\n: "))
math.add(a)
while True:
  i = i + 1
  x = input("+, -, *, / 입력하시오\n: ")
  if x in no_oper:
    b = 0
    cacul(b)
    break
  b = int(input(f"{i}번째 정수를 입력하세요\n: "))
  if b in no_oper:
    cacul(b)
    break
  cacul(b)
