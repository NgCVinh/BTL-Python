import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
Commits=[]
page=1
while True:
 try:
    Commit_data=requests.get(base_url+"commits",headers=header,params={"per_page":100,"page":page})
    if(Commit_data.status_code!=200):
        break
    Commit_page=Commit_data.json()
    if(not Commit_page):
        break
    Commits.extend(Commit_page)
    page+=1
 except requests.exceptions.Timeout:
    print('Time Error')
    break
 except requests.RequestException:
    print('RequestException')
    break
dict={}
for commit in Commits:
  try:
    info_commit=requests.get(f'{base_url}commits/{commit["sha"]}',headers=header,params={"per_page":100})
    if(info_commit.status_code==200):
        info_commit=info_commit.json()
        if(info_commit):
           for commit_file in info_commit["files"]:
               dict[commit_file["filename"]]=dict.get(commit_file["filename"],0)+1
  except requests.exceptions.Timeout:
      print('Time Error')
      break
  except requests.RequestException:
      print('RequestException')
      break
listFile=[]
for key,value in dict.items():
    listFile.append([key,value])
listFile=pd.DataFrame(listFile)
listFile.columns=["File","Commit"]
print(listFile)
listFile=listFile.sort_values(by="Commit",ascending=False)
listFile.to_excel(r"C:\Users\ASUS\Documents\Top_file_commit.xlsx")
print(listFile.head(5))

dict={}
for commit in Commits:
  try:
    info_commit=requests.get(f'{base_url}commits/{commit["sha"]}',headers=header,params={"per_page":100})
    if(info_commit.status_code==200):
        info_commit=info_commit.json()
        if(info_commit):
           for commit_file in info_commit["files"]:
               dict[commit_file["filename"]]=dict.get(commit_file["filename"],0)+commit_file["changes"]
  except requests.exceptions.Timeout:
      print('Time Error')
  except requests.RequestException:
      print('RequestException')
listFile=[]
for key,value in dict.items():
    listFile.append([key,value])
listFile=pd.DataFrame(listFile)
listFile.columns=["File","Changes"]
print(listFile)
listFile=listFile.sort_values(by="Changes",ascending=False)
listFile.to_excel(r"C:\Users\ASUS\Documents\Top_file_change.xlsx")
top_5_change=listFile.head(5)
plt.bar(top_5_change["Changes"],top_5_change["File"])
plt.show()
Files=[]
try:
  File_data=requests.get(base_url+"contents",headers=header,params={"per_page":100})
  File_data.raise_for_status()
  if(File_data.status_code==200):
    File_page=File_data.json()
    if(File_page):
      Files.extend(File_page)
except requests.exceptions.Timeout:
    print('Time Error')
except requests.RequestException:
    print('RequestException')
with open('File.json','w') as F:
   json.dump(Files,F,indent=4)    
list_File=[]
for file in Files:
    list_File.append([file["name"],file["size"]])
list_File=pd.DataFrame(list_File)
list_File.columns=["File","Size"]
list_File=list_File.sort_values(by="Size",ascending=False)
print(list_File)
list_File.to_excel(r"C:\Users\ASUS\Documents\Top_file_size.xlsx")
print(list_File["Size"].mean())
