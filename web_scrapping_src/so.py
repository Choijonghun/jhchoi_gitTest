import requests
from bs4 import BeautifulSoup

URL = f"https://lostark.game.onstove.com/Library/Tip/List?page=1&libraryStatusType=0&librarySearchCategory=0&searchTyappe=0&searchtext=&orderType=1&LibraryQaAnswerType=None"


def al_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    al_last_page = (pages[-1]).get_text
    print(al_last_page)


al_last_page()

#i_page = input("마지막 페이지를 입력하세요(정수) : ")
i_page = 155
URL = f"https://lostark.game.onstove.com/Library/TipLibrary/Tip/List?page={i_page}&libraryStatusType=0&librarySearchCategory=0&searchTyappe=0&searchtext=&orderType=1&LibraryQaAnswerType=None"

last_page = i_page


def extract_job(html):
    title = html.find("span", {"class": "list__title"})
    date = html.find("div", {"class": "list__date"})
    read = html.find("div", {"class": "list__read"})
    link = html.find("a")["href"]
    title = title.get_text(strip=True)
    date = date.get_text(strip=True)
    if read is None:
      read = "공지글"
    else:
      read = read.get_text(strip=True)
    link = str(link)
    
    return {
        'title': title,
        'date': date,
        'read' : read,
        "tip_link": f"https://lostark.game.onstove.com/{link}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"Scrapping SO: page : {page}")
      result = requests.get(
          f"https://lostark.game.onstove.com/Library/Tip/List?page={page+1}&libraryStatusType=0&librarySearchCategory=0&searchTyappe=0&searchtext=&orderType=1&LibraryQaAnswerType=None"
      )
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find("div", {"class": "list"}).find_all("li")
      for result in results:
          job = extract_job(result)
          jobs.append(job)#append가 뭔지 알아보기
    return (jobs)


def get_jobs():
    jobs = extract_jobs(last_page)
    return jobs