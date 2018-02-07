#coding: UTF-8
import requests, bs4
import re

def NormalizeURL(URL):
    # beta って書いてあったらこれを正規化
    betamatch = re.match(r"https://beta.atcoder.jp",URL)

    if betamatch:
        print("ベータだお")
        Contest_and_Problem = re.search(r"https://beta.atcoder.jp/contests/([a-zA-Z0-9]+)/tasks/(.+)",URL)
        print(Contest_and_Problem)
        ContestName = (Contest_and_Problem.group(1))
        ProblemName =  (Contest_and_Problem.group(2))
        alphaURL = "https://" + ContestName + ".contest.atcoder.jp/tasks/" + ProblemName
        print(alphaURL)
        return alphaURL
    else :
        print("ベータではないお")

        return URL


def GetSubmitID(URL):
    


    res = requests.get(URL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    submitbutton = soup.select('.btn.btn-primary.btn-large')
    subidtxt = submitbutton[0]["href"]
    pattern = r'[0-9]+'
    SubmitID = re.findall(pattern,subidtxt)[0]
    #<a class="btn btn-primary btn-large" href="/submit?task_id=3596"><span class="lang lang-selected"><span class="lang-en lang-child hidden-lang">Submit</span><span class="lang-ja lang-child">提出する</span></span></a>
    
    return SubmitID

#https://abc075.contest.atcoder.jp/tasks/abc075_c
# ttps://CONTESTNAME.contest.atcoder.jp/tasks/PROBLEMNAME
#https://beta.atcoder.jp/contests/abc075/tasks/abc075_c
# ttps://bera.atcoder.jp/CONTESTNAME/tasks/PROBLEMNAME

#みたいにおきかえればよい

#txt = str(input())
#URL = NormalizeURL(txt)
#print(GetSubmitID(URL))