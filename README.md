# CustomerMan
CustomerMan is a tool I created to manage my customers' subscriptions. It allows you to add a new customer, know all the customers who are currently subscribed, know the start and end date of a customer's subscription and much more.
It uses [Firebase](https://firebase.google.com/) Realtime Database, a free online NoSQL database.
## So you can use this tool even if you don't know anything about SQL!

# How to use it ?
## First,
You'll need to create and configure your Firebase database and retrieve your key in .json format. To do this :
* Access the Firebase console (https://console.firebase.google.com/).
* Create a new project or use an existing one.
* Go to the "Project Settings" section and download the configuration file (usually called serviceAccountKey.json).

## Then,
Once you've retrieved your key in .json format, simply drag and drop this file into the CustomerMan application folder.
![Alt text](https://cdn.discordapp.com/attachments/763090246912704512/1180080703531139132/image.png?ex=657c1ecc&is=6569a9cc&hm=2ff89b1c1b4040e5a56a1326ee84ecf0a47ff21cceab4f94ed774b0c762350bd&)

# ⬇️

![Alt text](https://cdn.discordapp.com/attachments/763090246912704512/1180081254096453662/image.png?ex=657c1f4f&is=6569aa4f&hm=5aabac0c52cdfd858a438703376592893e2f276936713f8a270d26d534d20a79&)

# Finaly,
The last step is to change the contents of the variable 'cred' by indicating the name of your json file which contains your key:
![Alt text](https://cdn.discordapp.com/attachments/763090246912704512/1180082390115287050/image.png?ex=657c205e&is=6569ab5e&hm=efc3f93ed24d87cd4958339253a102eb4979a2a009a27f34afdb9debfdac249b&)