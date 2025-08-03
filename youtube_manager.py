def list_all_videos(videos):
    print("*" * 50)
    for video in videos:
        print(f"{video}\n")
    print("*" * 50)

def add_video(videos):
    current_number_videos = len(videos)
    title = input("enter the title of the video: ")
    duration = input("enter the duration of the video: ")
    createdBy = input("enter the creator of the video: ")
    
    current_video = {
        "id": current_number_videos + 1,
        "title": title,
        "duration": duration,
        "createdBy": createdBy
    }
    
    videos.append(current_video)
    print("video is added successfully...")
    
def update_video(videos):
    if len(videos) <= 0:
        print("no added videos yet...!")
        return

    while True:
        video_id = int(input("enter the id of the video: "))
        if video_id <= len(videos):
            break
        print(f"video with give id:{video_id} doesn't exists")
    
    print(f"Note: updates will be reflected in the corresponding old ones...")
    new_title = input("enter a new title for the video (press enter, if you don't want): ")
    new_duration = input("enter a new duration for the video (press enter, if you don't want): ")
    new_createdBy = input("enter a new creator of the video (press enter, if you don't want): ")
    
    #[ {}, {}, {}, ... ]
    if new_title.strip() != "":
        print("title gets updated...!")
        for video in videos:
            if(video['id'] == video_id):
                video['title'] = new_title
                
    if new_duration.strip() != "":
        print("duration gets updated ...!")
        for video in videos:
            if(video['id'] == video_id):
                video['duration'] = new_duration
                
    if new_createdBy.strip() != "":
        print("createdBy gets updated...!")
        for video in videos:
            if(video['id'] == video_id):
                video['createdBy'] = new_createdBy                
    
def delete_video(videos):
    if len(videos) <= 0:
        print("no added videos yet...!")
        return
    
    while True:
        video_id = int(input("enter the id of the video: "))
        if video_id <= len(videos):
            break
        print(f"video with give id:{video_id} doesn't exists")
        
    for video in videos:
        if videos.index(video) == video_id:
            videos.remove(video)
            print(f"video with id:{video_id} and contents: {video} gets deleted...!")
            break
        
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
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _: # default case:
                print("Invalid option choosen, try again")

if __name__ == "__main__":
    main()