import requests
import numpy as np
import json
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
pulls=[]
page=1
state="all"
while True:
    try:
      pulls_data=requests.get(base_url+'pulls',headers=header,params={'per_page':100,'page':page,'state':state})
      if(pulls_data.status_code!=200):
         break
      page_pulls=pulls_data.json()
      if(not page_pulls):
         break
      pulls.extend(page_pulls)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
with open('pulls.json','w') as P:
   json.dump(pulls,P,indent=4)
print(len(pulls))
cant_merge=0
can_merge=0
Time_merge=np.array([])
for page_pulls in pulls:
    if(page_pulls["state"]=="closed"):
        if(page_pulls["merged_at"]==None):
          cant_merge+=1
        else:
          can_merge+=1
          from datetime import datetime
          time_merge=datetime.fromisoformat(page_pulls["merged_at"])
          time_open=datetime.fromisoformat(page_pulls["created_at"])
          Time_merge=np.append(Time_merge,time_merge-time_open)
print(can_merge)
print(cant_merge)

token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
commits=[]
page=1
while True:
    commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page})
    if(commits_data.status_code!=200):
        break
    page_commits=commits_data.json()
    if(not page_commits):
       break
    commits.extend(page_commits)
    page+=1
check_run=[]
for pull_request in pulls:
  try:
    sha=pull_request['head']['sha']
    sha_data=requests.get(f'{base_url}commits/{sha}/check-runs',headers=header,params={'per_page':100})
    if(sha_data.status_code==200):
       page_check_run=sha_data.json()
       if(page_check_run):
          check_run.append(page_check_run)
  except requests.exceptions.Timeout:
       print('Time Error')
       break
  except requests.RequestException:
       print('RequestException')
       break
success=0
failure=0
skipped=0
cancelled=0
failed=0
for Check in check_run:
   check_count=Check["total_count"]
   for check in Check["check_runs"]:
      if(check["conclusion"]=="skipped"):
         skipped+=1
         failure+=1
         break
      elif(check["conclusion"]=="success"):
         check_count-=1
      elif(check["conclusion"]=="failure"):
         failed+=1
         failure+=1
         break
      elif(check["conclusion"]=="cancelled"):
         cancelled+=1
         failure+=1
         break
      else:
         failure+=1
         break
   if(check_count==0):
      success+=1
print(failed)
print(skipped)
print(cancelled)
print(success)
print(failure)
import matplotlib.pyplot as plt
plt.figure(figsize=(100,50))
plt.pie([success,failure],labels=["Success pull requests","Failure pull requests"],autopct='%1.1f%%',textprops={'fontsize':10})
plt.show()