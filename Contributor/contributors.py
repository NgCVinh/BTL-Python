import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
Contributors=[]
page=1
while True:
    try:
      contributors_data=requests.get(base_url+'contributors',headers=header,params={'per_page':100,'page':page})
      if(contributors_data.status_code!=200):
         break
      page_contributors=contributors_data.json()
      if(not page_contributors):
         break
      Contributors.extend(page_contributors)
      page+=1
    except requests.exceptions.Timeout:
       print('Time Error')
       break
    except requests.RequestException:
       print('RequestException')
       break
with open('Contributors.json','w') as P:
   json.dump(Contributors,P,indent=4)
print(len(Contributors))
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
list_contributor=[]
for contributor in Contributors:
    list_contributor.append([contributor['login'],contributor['contributions']])
list_contributor=pd.DataFrame(list_contributor)
title=["Name","Contributions"]
list_contributor.columns=title
print(list_contributor)
list_contributor.to_excel(r"C:\Users\ASUS\Documents\Contributors.xlsx")
top_5_contributors=list_contributor.head(5)
top_5_contributors=top_5_contributors.assign(Percent=(top_5_contributors['Contributions']/len(commits))*100)
top_5_contributors.to_excel(r"C:\Users\ASUS\Documents\Percent_contributions.xlsx")
plt.figure(figsize=(100,50))
plt.pie(top_5_contributors['Contributions'],labels=top_5_contributors["Name"],autopct='%1.1f%%',textprops={'fontsize':10})
plt.show()
print(top_5_contributors)
commits_2021=[]
begin="1/1/2021"
end="31/12/2021"
page=1
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
commit_2021=[]
for contributor in Contributors:
    commit=0
    for Commit in commits_2021:
        if(Commit["commit"]["author"]["name"]==contributor['login']):
            commit+=1
    commit_2021.append([contributor['login'],commit])
commit_2021=pd.DataFrame(commit_2021)
title=["Name","Contributions"]
commit_2021.columns=title
commit_2021=commit_2021.sort_values(by="Contributions",ascending=False)
print(commit_2021)
commit_2021.to_excel(r"C:\Users\ASUS\Documents\Commit_2021.xlsx")
top_5_contributors_2021=commit_2021.head(5)
plt.bar(top_5_contributors_2021["Name"],top_5_contributors_2021["Contributions"])
plt.show()
print(top_5_contributors_2021)
commits_2022=[]
begin="1/1/2022"
end="31/12/2022"
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
commit_2022=[]
for contributor in Contributors:
    commit=0
    for Commit in commits_2022:
        if(Commit["commit"]["author"]["name"]==contributor['login']):
            commit+=1
    commit_2022.append([contributor['login'],commit])
commit_2022=pd.DataFrame(commit_2022)
title=["Name","Contributions"]
commit_2022.columns=title
commit_2022=commit_2022.sort_values(by="Contributions",ascending=False)
print(commit_2022)
commit_2022.to_excel(r"C:\Users\ASUS\Documents\Commit_2022.xlsx")
top_5_contributors_2022=commit_2022.head(5)
plt.bar(top_5_contributors_2022["Name"],top_5_contributors_2022["Contributions"])
plt.show()
print(top_5_contributors_2022)
commits_2023=[]
begin="1/1/2023"
end="31/12/2023"
page=1
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
commit_2023=[]
for contributor in Contributors:
    commit=0
    for Commit in commits_2023:
        if(Commit["commit"]["author"]["name"]==contributor['login']):
            commit+=1
    commit_2023.append([contributor['login'],commit])
commit_2023=pd.DataFrame(commit_2023)
title=["Name","Contributions"]
commit_2023.columns=title
commit_2023=commit_2023.sort_values(by="Contributions",ascending=False)
print(commit_2023)
commit_2023.to_excel(r"C:\Users\ASUS\Documents\Commit_2023.xlsx")
top_5_contributors_2023=commit_2023.head(5)
print(top_5_contributors_2023)
plt.bar(top_5_contributors_2023["Name"],top_5_contributors_2023["Contributions"])
plt.show()