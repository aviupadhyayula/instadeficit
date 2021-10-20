import instaloader
import getpass

def sign_in():
    global username
    username = input("Username: ")
    L = instaloader.Instaloader()
    L.login(username, getpass.getpass(prompt="Password: "))
    return L

def get_lists(L):
    profile = instaloader.Profile.from_username(L.context, username)
    global followers
    followers = []
    global followees 
    followees = []
    for follower in profile.get_followers():
        followers.append(follower)
    for followee in profile.get_followees():
        followees.append(followee)

def find_deltas():
    global unfollowers
    unfollowers = []
    for followee in followees:
        found = False
        for follower in followers:
            if follower == followee:
                found = True
                break
        if found == False:
            unfollower = format_name(followee)
            unfollowers.append(unfollower)

def display_deltas():
    print("People to unfollow:")
    for unfollower in unfollowers:
        print(" - " + unfollower)


def format_name(profile):
    name = str(profile)
    name = name[9 : name.index('(') - 1]
    return name

def main():
    get_lists(sign_in())
    find_deltas()
    display_deltas()

if __name__ == "__main__":
    main()
