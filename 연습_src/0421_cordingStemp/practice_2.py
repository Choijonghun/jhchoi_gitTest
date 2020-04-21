'''
li = []
def numMulti(m):
  result = 1
  for a in str(m):
    result *= int(a)
  return result

for num in range(10,1001,1):
  re = numMulti(num)
  li.append(re)
li = sum(li)
print(li)
'''
print(eval('+'.join('*'.join(str(x)) for x in range(10, 1001))))
