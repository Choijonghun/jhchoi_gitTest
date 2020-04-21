'''
#main.py
from modulation import modul as m
m()
'''

def read():
  with open("ori.txt", "r") as f: #원본 파일
    lines = f.readlines()
  return lines

def write(line):
  with open("Question_5.py", "a") as f2: #변환 파일
    if line == "\n":
      f2.write(f"{line}")
    else:
      f2.write(f"#{line}")
  return line

def modul():
  lines = read()
  for line in lines:
    write(line)