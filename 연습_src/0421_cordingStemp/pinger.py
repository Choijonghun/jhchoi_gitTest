#I am 타노스
import random

a = [2, 3, 1, 6, 5, 7, 4] #입력

if len(a) % 2 == 0:  n = len(a)/2
else:  n = len(a)/2 + round(random.uniform(0,1),0)
print(random.sample(a,int(n)))
