#coding: UTF-8
import requests, bs4
import re

def GetSubmitID(URL):
    
    URL = "https://abc075.contest.atcoder.jp/tasks/abc075_c"
    res = requests.get(URL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    submitbutton = soup.select('.btn.btn-primary.btn-large')
    subidtxt = submitbutton[0]["href"]
    pattern = r'[0-9]+'
    SubmitID = re.findall(pattern,subidtxt)[0]
    #print("Submit ID is,",SubmitID)
    #print(type(SubmitID))
    #<a class="btn btn-primary btn-large" href="/submit?task_id=3596"><span class="lang lang-selected"><span class="lang-en lang-child hidden-lang">Submit</span><span class="lang-ja lang-child">提出する</span></span></a>
    
    return SubmitID



#sub = "a"
#print(function(sub))

