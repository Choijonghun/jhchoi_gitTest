#CSV (Comma Separated Values)
import csv

def save_so_file(so_jobs):
  file = open("so_jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["제목","날짜", "조회수", "tip_link"])
  for job in so_jobs:
     writer.writerow(list(job.values()))
  return

def save_in_file(in_jobs):
  file = open("in_jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company", "location", "link"])
  for job in in_jobs:
     writer.writerow(list(job.values()))
  return
