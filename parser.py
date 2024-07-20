import json

followers_fp = 'followers_1.json'
following_fp = 'following.json'

# grabbing json files
with open(followers_fp, 'r') as file:
    followers = json.load(file)

with open(following_fp, 'r') as file:
    following = json.load(file)

followers_list = []
for el in followers:
    followers_list.append(el.get("string_list_data")[0].get("value"))
following_list = []
for ele in following.get("relationships_following"):
    following_list.append(ele.get("string_list_data")[0].get("value"))



whos_not_followings_me_back = set(following_list) - set(followers_list)

for entry in whos_not_followings_me_back:
    print(entry)

with open("whos_not_following_me_back_list.txt", 'w') as file:
    for entry in whos_not_followings_me_back:
        file.write(f"{entry}\n")
