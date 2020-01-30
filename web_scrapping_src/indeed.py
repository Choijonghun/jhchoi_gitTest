import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%EC%98%81%EC%96%B4&limit={LIMIT}"


def get_last_pages():
    result = requests.get(URL)
    #url의 모든 html을 추출
    #html에서 정보를 추출 하기 위해
    #beautifulsoup4 패키지 설치 후 import
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    #page의 리스트를 추출함
    pages = []  #배열 함수 정의
    for link in links[0:-1]:  #span을 모두 가져오되 마지막 것을 제외
        pages.append(int(link.string))  #span배열에 page를 하나씩 넣어줌
    #span의 마지막 배열에는 페이지 넘버가 아닌 '다음'이 들어가있었음
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("span", {"class": "location"}).string
    job_id = html["data-jk"]
    return {
        'title':        title,
        'company':        company,
        'location':        location,
        'link':        f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%EC%98%81%EC%96%B4&limit=50&vjk={job_id}"
    }


def get_job(last_pages):
    jobs = []
    for page in range(last_pages):
      print(f"Scrapping indeed : page : {page}")
      result = requests.get(f"{URL}&start={page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
      for result in results:
          job = extract_job(result)
          jobs.append(job)
    return jobs

def get_jobs():
  last_pages = get_last_pages()
  jobs = get_job(last_pages)
  return jobs