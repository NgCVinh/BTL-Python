import requests
import pandas as pd
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
issues_open=[]
state='open'
page=1
while True:
    try:
      issues_data=requests.get(base_url+'issues',headers=header,params={'per_page':100,'page':page,'state':state})
      if(issues_data.status_code!=200):
         break
      page_issues_open=issues_data.json()
      if(not page_issues_open):
         break
      issues_open.extend(page_issues_open)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
print(issues_open)
issues_closed=[]
state='closed'
page=1
while True:
    try:
      issues_data=requests.get(base_url+'issues',headers=header,params={'per_page':100,'page':page,'state':state})
      if(issues_data.status_code!=200):
         break
      page_issues_closed=issues_data.json()
      if(not page_issues_closed):
         break
      issues_closed.extend(page_issues_closed)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
print(len(issues_closed))
import numpy as np
import json
issues=[]
page=1
state="all"
while True:
    try:
      issues_data=requests.get(base_url+'issues',headers=header,params={'per_page':100,'page':page,'state':state})
      if(issues_data.status_code!=200):
         break
      page_issues_all=issues_data.json()
      if(not page_issues_all):
         break
      issues.extend(page_issues_all)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
with open('Issues.json','w') as I:
   json.dump(issues,I,indent=4)
print(len(issues))
import numpy as np
can_solve=0
cant_solve=0
Date=np.array([])
for page_issues in issues:
    if(page_issues["closed_at"]==None):
        cant_solve+=1
    else:
        can_solve+=1
        from datetime import datetime
        closed_at_datetime = datetime.fromisoformat(page_issues["closed_at"])
        created_at_datetime=datetime.fromisoformat(page_issues["created_at"])
        Date=np.append(Date,closed_at_datetime-created_at_datetime)
print(Date.mean())
enhancement=0
bug=0
for page_issues in issues:
    for element in page_issues["labels"]:
       if(element["name"]=="🐛 bug"):
          bug+=1
       elif(element["name"]=="✨ enhancement"):
          enhancement+=1
print(bug)
print(enhancement)