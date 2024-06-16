import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
commits=[]
page=1
while True:
    try:
      commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page})
      if(commits_data.status_code!=200):
         break
      page_commits=commits_data.json()
      if(not page_commits):
         break
      commits.extend(page_commits)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
with open('Commits.json','w') as C:
   json.dump(commits,C,indent=4)
print(len(commits))
Commit_years=[]
Contributor_years=[]
for j in range(2021,2024):
    for i in range(1,5):
       if(i==1)or(i==3) or(i==4):
          begin=f"1/{3*(i-1)+1}/2021"
          end=f"31/{3*(i-1)+3}/{j}"
       elif(i==2):
          begin=f"1/{3*(i-1)+1}/2021"
          end=f"30/{3*(i-1)+3}/{j}"
       page=1
       Commit=[]
       try:
        while True:
          commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page,'since':begin,'until':end})
          if(commits_data.status_code!=200):
            break
          page_commits=commits_data.json()
          if(not page_commits):
            break
          Commit.extend(page_commits)
          page+=1
       except requests.exceptions.Timeout:
        print('Time Error')
        break
       except requests.RequestException:
        print('RequestException')
        break
       Contributor={}
       Contributor=set(Contributor)
       for commit in Commit:
          Contributor.add(commit["commit"]["author"]["name"])
       Commit_years.append(len(Commit))
       Contributor_years.append(len(Contributor))
labels=["Spring 2021","Summer 2021","Autumn 2021","Winter 2021","Spring 2022","Summer 2022","Autumn 2022","Winter 2022","Spring 2023","Summer 2023","Autumn 2023","Winter 2023"]
plt.plot(labels,Commit_years,label="Commits",color='red')
plt.plot(labels,Contributor_years,label="Contributors",color='blue')
plt.legend()
plt.show()


begin="1/1/2021"
end="31/12/2021"
page=1
commits_2021=[]
while True:
  try:
    commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page,'since':begin,'until':end})
    if(commits_data.status_code!=200):
        break
    page_commits=commits_data.json()
    if(not page_commits):
       break
    commits_2021.extend(page_commits)
    page+=1
  except requests.exceptions.Timeout:
      print('Time Error')
      break
  except requests.RequestException:
      print('RequestException')
      break


begin="1/1/2022"
end="31/12/2022"
commits_2022=[]
page=1
while True:
  try:
    commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page,'since':begin,'until':end})
    if(commits_data.status_code!=200):
        break
    page_commits=commits_data.json()
    if(not page_commits):
       break
    commits_2022.extend(page_commits)
    page+=1
  except requests.exceptions.Timeout:
    print('Time Error')
    break
  except requests.RequestException:
    print('RequestException')
    break
begin="1/1/2023"
end="31/12/2023"
page=1
commits_2023=[]
while True:
  try:
    commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page,'since':begin,'until':end})
    if(commits_data.status_code!=200):
        break
    page_commits=commits_data.json()
    if(not page_commits):
       break
    commits_2023.extend(page_commits)
    page+=1
  except requests.exceptions.Timeout:
    print('Time Error')
    break
  except requests.RequestException:
    print('RequestException')
    break








Commit_month=[]
Month=[]
cnt=0
for i in range(1,13):
    if(i==1)or (i==3)or(i==5)or(i==7)or(i==8)or(i==10)or(i==12):
        begin=f'1/{i}/2023'
        end=f'31/{i}/2023'
    elif (i==2):
        begin=f'1/{i}/2023'
        end=f'28/{i}/2023'
    else:
        begin=f'1/{i}/2023'
        end=f'30/{i}/2023'
    commit=[]
    page=1
    while True:
      try:
        commits_data=requests.get(base_url+'commits',headers=header,params={'per_page':100,'page':page,'since':begin,'until':end})
        if(commits_data.status_code!=200):
          break
        page_commits=commits_data.json()
        if(not page_commits):
          break
        commit.extend(page_commits)
        page+=1
      except requests.exceptions.Timeout:
          print('Time Error')
          break
      except requests.RequestException:
          print('RequestException')
          break
    Month.append(f"Tháng {i}")
    Commit_month.append(len(commit))
import matplotlib.pyplot as plt
plt.bar(Month,Commit_month)
plt.show()


