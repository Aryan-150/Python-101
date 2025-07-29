def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = []
    while True:
        print("Youtube Manager application")
        print("1. list all your favorite yt-videos.")
        print("2. add a new yt-video to your favorites.")
        print("3. update a yt-video details from favorites.")
        print("4. delete a yt-video from favorites.")
        print("5. exit the application.")
        
        choice = input("Enter your choice from the above given choices: ")
        
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _: # default case:
                print("Invalid option choosen, tyr again")

if __name__ == "__main__":
    main()