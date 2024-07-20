# Instagram- WhoDoesn'tFollowMeBack

## About
A simple tool that produces a `.txt` file containing a list of instagram usernames that don't follow you back.

## Tutorial

### Step 1: Configuring your data

Navigate to your instagram profile and click on the 3 lines that say "more":

On Desktop:     
<img src="https://github.com/user-attachments/assets/02d83dd0-e4ff-4bb3-afed-ab36099e5f15" alt="Desktop view" width="200">

Select "Your activity" and *(on mobile scroll down)* select "Download your information":

<img src="https://github.com/user-attachments/assets/53e761bb-8d84-4c5b-8db9-3d27d1def8de" alt="Mobile view" width="200">

Select "Download or transfer information": 

<img src="https://github.com/user-attachments/assets/35193164-09ca-4ca1-94d8-15b416d8612f" alt="Download or transfer information" width="300">

You don't need all of your account data only some, so select "Some of your information":

<img src="https://github.com/user-attachments/assets/ac553bfa-9179-471b-8750-61f6f1eddd58" alt="Some of your information" width="300">

Select "Followers and following":

<img src="https://github.com/user-attachments/assets/09e91702-fc60-4af9-8475-f35248cfce63" alt="Followers and following" width="300">

Recommend downloading your data to your device but feel free to choose another location:

<img src="https://github.com/user-attachments/assets/3c04c7df-a069-4441-973c-0c96057ac7d2" alt="Download to your device" width="300">

Ensure that the time range is set on "All time":

<img src="https://github.com/user-attachments/assets/2b862603-fdca-4737-9eb0-25ea37fe2957" alt="All time" width="300">

Ensure that the format is "JSON":

<img src="https://github.com/user-attachments/assets/962a25e6-d709-4d12-ba1f-85020b8d9506" alt="JSON format" width="300">

Finally click on "Create files":

<img src="https://github.com/user-attachments/assets/b1213fb4-499d-4ce7-b436-934f1267e727" alt="Create files" width="300">


### Step 2: Downloading your data

After some time your instagram data will be available for download:
![image](https://github.com/user-attachments/assets/8ab782db-7b39-43f3-a9eb-85746a458b39)

Selecting download will download a zip file with a "followers_1.json" file and a "following.json" file.

### Step 3: Running the script

Clone this repository to your device and add your "followers_1.json" and "following.json" files to the same directory. 

Run the `parser.py` script which will produce a `whos_not_following_me_back_list.txt` file which contains a list of the usernames that you follow on instagram that don't follow me back. 






