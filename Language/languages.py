
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
Language=[]
try:
  Laguage_data=requests.get(base_url+"languages",headers=header,params={'per_page':100})
  if(Laguage_data.status_code==200):
     Language_page=Laguage_data.json()
     if(Language_page):
       Language.extend([Language_page])
except requests.exceptions.Timeout:
    print('Time Error')
except requests.RequestException:
    print('RequestException')
with open('Language.json','w') as L:
   json.dump(Language,L)
print(Language)
List_language=[]
for language in Language[0]:
    List_language.append([language,Language[0][language]])
List_languages=pd.DataFrame(List_language)
List_languages.columns=["Language","Number"]
print(List_languages)
List_languages.to_excel(r"C:\Users\ASUS\Documents\Language.xlsx")
top_3_language=[]
top=0
other=0
for language in Language[0]:
    if(top<3):
        top_3_language.append([language,Language[0][language]])
    else:
        other+=Language[0][language]
    top+=1
top_3_language.append(["Other",other])
List_top3_languages=pd.DataFrame(top_3_language)
List_top3_languages.columns=["Language","Number"]
print(List_top3_languages)
List_top3_languages.to_excel(r"C:\Users\ASUS\Documents\Top_3_languages.xlsx")
plt.figure(figsize=(100,50))
plt.pie(List_top3_languages["Number"],labels=List_top3_languages["Language"],autopct='%1.1f%%',textprops={'fontsize':10})
plt.show()
