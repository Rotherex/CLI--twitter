import tweepy
import requests
import os

## Initialising tokens


def read_tokens():
    global tokens
    if os.path.exists("token.txt"):
        tokenfileread = open("token.txt", 'r+')
        tokens = tokenfileread.readlines()
        for token in tokens:
            tokens[tokens.index(token)] = token.replace("\n", "")
        tokenfileread.close()
    else:
        tokenfileread = open("token.txt", "a")
        tokenfileread.write("apikey\n apisecret\n access\n accesstoken")
        tokenfileread.close()
        read_tokens()
        

def main():
    read_tokens()
    print("1: Send an Tweet.")
    print("2: Send an Tweet with an Image.")
    print("3: Get API token info.")
    print("4: Setup your Twitter token.")
    print("5: Get User Info inside a .txt file.")
    print("6: Quit")
    selection = input()
    send_wizard(selection)

def send_Tweet(message):
    auth = tweepy.OAuthHandler(tokens[0], tokens[1])
    auth.set_access_token(tokens[2], tokens[3])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    api.update_status(message)

def send_Image_Tweet(url, message):
    auth = tweepy.OAuthHandler(tokens[0], tokens[1])
    auth.set_access_token(tokens[2], tokens[3])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
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

def token_setup():
    print("To register an application in twitter, you can always go to developer.twitter.com and create an application there.")
    confirm = input("Would you like to proceed to setup? This will clear all your existing tokens! (Y/N) ")
    if confirm == "Y" or confirm == "y":
        api_key = input("Enter the API Key: ")
        api_key_secret = input("Enter the API Key Secret: ")
        access_token = input("Enter the Access Token: ")
        access_token_secret = input("Enter the Access Token Secret: ")
        tokens = [api_key, api_key_secret, access_token, access_token_secret]
        tokenfile = open("token.txt", 'r+')
        tokenfile.truncate(0)
        for token in tokens:
            if tokens.index(token) == tokens[-1]:
                tokenfile.write(token)
            else:
                tokenfile.write(token + "\n")
        tokenfile.close()
        print("Tokens have been written!")
        print("Going back to the main menu...")
        main()
    else:
        print("Cancelling setup.")
        main()

def get_User_Info(userName):
    auth = tweepy.OAuthHandler(tokens[0], tokens[1])
    auth.set_access_token(tokens[2], tokens[3])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.get_user(userName)

    print("User's Name is: " + user.name)
    print("User's Description is: " + user.description)

    print("Followers amount is: " + str(user.followers_count))

    for friendsCount in user.friends():
        friendsCount += 1
    
    print("Following Count is:" + str(friendsCount))

    print("Do you want to save those statistics into a .txt file? (Y/N)")
    userChoice = input()
    if userChoice == "Y" or "y":
        filename = str(user.screen_name)+".txt"
        with open(filename, "w+") as f:
            f.write("User's Name is: " + user.name)
            f.write("\nUser's Description is: " + user.description)
            f.write("\nFollowers amount is: " + str(user.followers_count))
            f.write("\nFollowing Count is: " + str(friendsCount))
    elif userChoice == "N" or "n":
        print("Alright. Going back to the main menu")
        main()
    else:
        print("Wrong Choice! Going back to the main menu.")
        main()


# Sending logic
def send_wizard(x):

    if x == "1":
        print("Selected: 1: Send an Tweet")
        print("What message do you want to send?")
        message = input()
        print("Ready to send your message, : " + message + " ?")
        print("Y/N")
        userChoice1 = input()
        if userChoice1 == "Y" or "n":
            send_Tweet(message)
        elif userChoice1 == "N" or "n":
            print("Going back to the menu.")
            main()
        else:
            print("Invalid Character. Going back to the menu.")
            main()
    elif x == "2":
        print("Selected 2: Send an Tweet with an Image")
        print("What image do you want to send? (Direct URL link)")
        url = input()
        print("Are you sure this is an direct link?")
        print("Y/N")
        userChoice1 = input()
        if userChoice1 == "Y" or "n":
            print("Alright, got it. Now what message do you want to add to the image tweet?")
            urlMessage = input()
            print(urlMessage + ". Is that the message you want to add?")
            userChoice2 = input()
            if userChoice2 == "Y" or "n":
                print(url + "Is the image link, and \"" + urlMessage + "\" is the message you want to send, do you want to send? (Y/N)")
                userChoice3 = input()
                if userChoice3 == "Y" or "y":
                    send_Image_Tweet(url, urlMessage)
                elif userChoice3 == "N" or "n":
                    print("Alright. Going back to the menu.")
                    main()
                else:
                    print("Wrong Choice! Going back to the menu.")
                    main()
            elif userChoice2 == "N" or "n":
                print("Alright. Going back to the menu.")
                main()
            else:
                print("Wrong Choice! Going back to the menu.")
                main()
        elif userChoice1 == "N" or "n":
            print("Alright. Going back to the menu.")
            main()
        else:
            print("Wrong Choice! Going back to the menu.")
            main()
    elif x == "3":
        print("API KEY is " + tokens[0])
        print("API KEY SECRET is " + tokens[1])
        print("ACCESS TOKEN is " + tokens[2])
        print("ACCESS TOKEN SECRET is " + tokens[3])
        main()
    elif x == "4":
        print("Running the twitter token wizard..")
        token_setup()
    elif x == "5":
        print("Input an Name of the User you want to get data from.")
        userName = input()
        print("Are you Sure? (Y/N)")
        userChoice4 = input()
        if userChoice4 == "Y" or "n":
            get_User_Info(userName)
        elif userChoice4 == "N" or "n":
            print("Alright. Reopening Main Menu.")
            main()
        else:
            print("Invalid choice. Going back to the Main Menu.")
            main()

    elif x == "6":
        print("Quitting.")
        exit()
    else:
        print("Invalid choice. Reopening Main Menu.")
        main()

    
# made by clima (clima ;-;#8707) and simonknowsstuff (simonknowsstuff#7501)

main()
