#Q1
#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def Q1():
  a = input("정수를 입력하세요\n:")
  a = int(a)
  if a % 2 == 1:
    print("홀수 입니다.")
  else:
    print("짝수입니다.")


#Q2
#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
#※ 평균 값을 구할 때 len 함수를 사용해 보자.

def q2_input(): #input을 받아 리스트 형태로 li에 저장
  li = []
  i = 1
  while i != 100:
    b = int(input("정수를 입력하세요. (0을 입력하면 입력이 종료 됩니다.):"))
    if b == 0: #input이 0 이라면 종료
      break
    else: #input이 정수라면 li에 추가
      li.append(b)
  return li

def q2_calculate(li): #리스트 li를 매개변수로 받아옴
  total = 0
  for c in li: #리스트의 원자를 하나씩 추출하여 total에 저장
    total = c + total
  avg = total / len(li)
  print("총 합은 :\n", total)
  print("평균은 :")
  return avg

def Q2():
  li = q2_input()
  result = q2_calculate(li)
  print(result)
  return result

#Q3
#다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.#이 프로그램을 수행해 보자.
#첫번째 숫자를 입력하세요:3
#두번째 숫자를 입력하세요:6
#두 수의 합은 36 입니다
#3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
#※ int 함수를 사용해 보자.
def Q3():
  input1 = int(input("첫번째 숫자를 입력하세요:"))
  input2 = int(input("두번째 숫자를 입력하세요:"))
  total = input1 + input2
  print("두 수의 합은 %s 입니다" % total)

#Q4
#다음 중 출력 결과가 다른 것 한 개를 골라 보자.
#답 3번
def Q4():
  print("you" "need" "python") #youneedpython
  print("you"+"need"+"python") #youneedpython
  print("you", "need", "python") #you need python
  print("".join(["you", "need", "python"])) #youneedpython

#Q5
#다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
#이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

#답 : f1을 열어주고 닫는 구문이 없었음
def Q5():
  f1 = open("test.txt", 'w')
  f1.write("Life is too short")
  f1.close() #답 : 이 행을 추가
  f2 = open("test.txt", 'r')
  print(f2.read())



#Q6
#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
def Q6():
  while True:
    a = input("텍스트 작성 : ")
    if a == '':
      print("종료")
      break
    f1 = open("test.txt", 'a')
    f1.write(a+"\n")
    f1.close() #답 : 이 행을 추가
    f2 = open("test.txt", 'r')
    print(f2.read())


#Q7
#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
#※ replace 함수를 사용해 보자.
#Life is too short
#you need java
def Q7():
  f = open('test.txt', 'r') #파일을 먼저 읽어 옴
  body = f.read() #읽어 온 파일을 body에 저장
  f.close()

  body = body.replace('java', 'python') #body값을 replace 함수로 값을 변경
  f = open('test.txt', 'w')
  f.write(body)
  f.close()
  f2 = open("test.txt", 'r')
  print(f2.read())
