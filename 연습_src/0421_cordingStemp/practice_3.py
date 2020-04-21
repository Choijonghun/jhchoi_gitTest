#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ... 과 같이, 0 이상의 앞뒤가 같은 수를 크기 순으로 나열할 때, n 번째 수를 계산하는 프로그램을 작성하라.
'''count = int(input("시작\n"))
pal_list=[]
num = 0

def dec_pal(num):
  a = list(str(num))
  b = list(reversed(a))
  if a==b:
    pal_list.append(num)

while len(pal_list) < count:
# palindromic number list의 수가 지정한 숫자에 이를 때까지 리스트에 palindrome 추가
  dec_pal(num)
  num += 1
print(pal_list[-1])
'''
i = '1032002305'
a = list(i)
b = list(reversed(a))

if a == b:
  print("True")

if str(i) ==str(i)[::-1]:
  print("TTrue")
print(str(i)[::-1])

