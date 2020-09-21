import tweepy
import requests
import os

# https://851028.smushcdn.com/1862890/wp-content/uploads/2020/06/facts-about-mountains-840x490.jpg?lossy=1&strip=1&webp=1
# first link

# http://www.inspire-travel.com/wp-content/uploads/2020/01/Waterfalls-1050x748.jpg
# second link

#Authenticate
auth = tweepy.OAuthHandler("YLp44QDJH8WzsNlmCznhcXmAT", "aPoYZIj0zLjtt6yaqLKvfJbGkqadetQwcGkducbqqyQF4nrNNJ")
auth.set_access_token("885771179356819457-L2pq3Za7fU8EDjDSjKGPAhI3UCkPi4N", "dcypB2cSnAh6f3caE8Hf9PA9EUQxps8iT5ON8uxoANuNx")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def send_Tweet(message):
    api.update_status(message)

def send_Image_Tweet(url, message):
    filename = "temp.jpg"
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Error! Unable to download image.")

def get_Timeline():
    timeline = api.home_timeline()
    filename = 'recent-timeline.txt'
    with open(filename, 'w+') as f:
        for tweet in timeline:
            message = f"{tweet.user.name} said: {tweet.text}".encode("utf-8")
            f.write(str(message))
    return timeline

def main_Menu():
    print("Hello, it is me - Your Command Line Twitter!")
    print("What do you want to do?")
    print("1: Send an Tweet")
    print("2: Send an Tweet with an Image")
    print("3: Get your timeline (20 latest messages on your main twitter screen)")
    x = input()
    return x

x = main_Menu()

if x == "1":
    print("Selected: 1: Send an Tweet")
    print("What message do you want to send?")
    message = input()
    print("Ready to send your message, : " + message + " ?")
    print("Y/N")
    userChoice1 = input()
    if userChoice1 == "Y":
        send_Tweet(message)
    elif userChoice1 == "N":
        print("Alright. Going back to the menu.")
        main_Menu()
    else:
        print("Wrong Choice! Going back to the menu.")
        main_Menu()
elif x == "2":
    print("Selected 2: Send an Tweet with an Image")
    print("What image do you want to send? (Direct URL link)")
    url = input()
    print("Are you sure this is an direct link?")
    print("Y/N")
    userChoice1 = input()
    if userChoice1 == "Y":
        print("Alright, got it. Now what message do you want to add to the image tweet?")
        urlMessage = input()
        print(urlMessage + " Is that the message you want to add?")
        userChoice2 = input()
        if userChoice2 == "Y":
            print(url + "Is the image link, and " + urlMessage + "Is the message you want to send, do you want to send?")
            print("Y/N")
            userChoice3 = input()
            if userChoice3 == "Y":
                send_Image_Tweet(url, urlMessage)
            elif userChoice3 == "N":
                print("Alright. Going back to the menu.")
                main_Menu()
            else:
                print("Wrong Choice! Going back to the menu.")
                main_Menu()
        elif userChoice2 == "N":
            print("Alright. Going back to the menu.")
            main_Menu()
        else:
            print("Wrong Choice! Going back to the menu.")
            main_Menu()
    elif userChoice1 == "N":
        print("Alright. Going back to the menu.")
        main_Menu()
    else:
        print("Wrong Choice! Going back to the menu.")
        main_Menu()
elif x == "3":
    timeline = get_Timeline()
    pass
    
