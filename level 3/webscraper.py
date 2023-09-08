from bs4 import BeautifulSoup
import requests
import time

#input skill from user
user_skills=(input("enter your skills:").lower().replace(","," ")).split()

#function for finding jobs
def find_jobs(skills):

    #requesting the webpage
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    #intilalizing soup object with parcel lxml
    soup=BeautifulSoup(html_text,'lxml')

    #finding jobs the specific information based on html class and other tags
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        pub_date=job.find('span',class_="sim-posted").span.text
        if "few" in pub_date:
            company_name=job.find('h3',class_="joblist-comp-name").text.replace(" ","").strip()
            skills=job.find('span',class_="srp-skills").text.replace(" ","").strip()
            pub_date=job.find('span',class_="sim-posted").span.text
            more_info=job.header.h2.a['href']
            for skill in user_skills:
                if skill in skills:

                    #creating a file and storing info in a file
                    with open(f'jobs_folder/{index}.txt','w') as f:
                        f.write(f'company_name: {company_name}\n')
                        f.write(f'required_skills: {skills}\n')
                        f.write(f'more_info: {more_info}\n')
                    print(f'file saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs(user_skills)
        time_wait=10
        print(f'waiting {time_wait}seconds')
        time.sleep(3*60)


