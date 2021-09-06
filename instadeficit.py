import instaloader
import getpass

# getting user input
username = input("Username: ")
# logs in to instaloader session
L = instaloader.Instaloader()
# password is gotten via getpass; it's not locally stored, cannot be read, and is hashed
L.login(username, getpass.getpass(prompt="Password: "))
profile = instaloader.Profile.from_username(L.context, username)
# scrapes followers and followees
followers = []
followees = []
for follower in profile.get_followers():
    followers.append(follower)
for followee in profile.get_followees():
    followees.append(followee)
# catalogs followees who do not appear in list of followers
unfollowers = []
for followee in followees:
    found = False
    for follower in followers:
        if (follower == followee):
            found = True
    if (found == False):
        unfollower = str(followee)
        unfollower = unfollower[9 : unfollower.rfind('(') - 1]
        unfollowers.append(unfollower)
# displays list of unfollowers
print("People to unfollow:")
for unfollower in unfollowers:
    print("  - " + unfollower)