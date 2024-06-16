import requests
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
token="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"
owner="starship"
repo="starship"
base_url=f'https://api.github.com/repos/{owner}/{repo}/'
header={'Authorization':f'token {token}'}
pulls=[]
page=1
state="all"
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
dict={}
for commit in commits:
   dict[commit["commit"]["author"]["name"]]=set({})
for commit in commits:
   for line in commit["commit"]["message"].split("\n"):
     if line.startswith('Co-authored-by:'):
       for word in line.split():
         if not (word.startswith('Co-authored-by') or word.startswith('<')):
           dict[commit["commit"]["author"]["name"]].add(word)
relation=[]
for person,co_author in dict.items():
   relation.append([person,len(co_author)])
relation_board=pd.DataFrame(relation)
relation_board.columns=["Name","Co-author"]
relation_board=relation_board.sort_values(by="Co-author",ascending=False)
print(relation_board)
relation_board.to_excel(r"C:\Users\ASUS\Documents\Relationship.xlsx")
tmp=[]
for person in dict:
    for contributor in dict[person]:
      if((person,contributor) not in tmp) and ((contributor,person) not in tmp) and(contributor!=person):
        tmp.append((person,contributor))

top_5_relationship=relation_board.head(5)
plt.bar(top_5_relationship["Name"],top_5_relationship["Co-author"])
plt.show()

G=nx.Graph()
G.add_edges_from(tmp)
nx.draw(G,nx.kamada_kawai_layout(G),with_labels=True, node_size=10,edge_color='grey')
plt.figure(figsize=(50,50))
plt.show()



