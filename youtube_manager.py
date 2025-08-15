import json

def list_all_videos(FILE_NAME):
    try:
        videos = get_videos(FILE_NAME)  # videos is list
        print("*" * 30)
        for video in videos:
            print(f"{video["id"]}. --> {video["title"]}, {video["duration"]}, {video["createdBy"]}")
        print("*" * 30)
    except TypeError:
        print(f"error while displaying the videos...!")
    
def add_video(FILE_NAME):
    try:
        videos = get_videos(FILE_NAME)
        while True:
            title = input("enter the title of the video: ")
            duration = input("enter the duration of the video: ")
            createdBy = input("enter the owner of the video: ")

            if title.strip() != "" and duration.strip() != "" and createdBy.strip() != "":
                break
                
        videos.append({
            "id": videos.__len__(),
            "title": title,
            "duration": duration,
            "createdBy": createdBy
        })
        set_videos(FILE_NAME, videos)
        print(f"new video added...!\n")
    except:
        print("error")

def update_video(FILE_NAME):
    list_all_videos(FILE_NAME)
    videos = get_videos(FILE_NAME)
    update_video_request_count = 0
    while True:
        if update_video_request_count >= 3:
            response = input("would you like to return to home (y/n): ")
            if response.strip() == "y":
                return
            
        video_id = int(input("enter the video-id you want to update:"))
        if 0 <= video_id <= len(videos) - 1:
            break
        update_video_request_count += 1
    
    for video in videos:
        print(video)
        if video["id"] == video_id:
            new_title = input("enter the new title (leave blank if you don't want to: )")
            new_duration = input("enter the new duration (leave blank if you don't want to: )")
            new_createdBy = input("enter the new createdBy (leave blank if you don't want to: )")

            if new_title.strip() != "":
                video["title"] = new_title
            if new_duration.strip() != "":
                video["duration"] = new_duration
            if new_createdBy.strip() != "":
                video["createdBy"] = new_createdBy

    set_videos(FILE_NAME, videos)
    print(f"updated the details of video-id: {video_id}\n")

def delete_video(FILE_NAME):
    videos = get_videos(FILE_NAME)
    while True:
        video_id = int(input("enter the video-id you want to delete: "))
        if 0 <= video_id <= len(videos):
            break
    videos.remove(videos[video_id])
    set_videos(FILE_NAME, videos)
    print(f"video with video-id:{video_id} removed...!\n")

def set_videos(FILE_NAME, videos):
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(videos, file, indent=4)
    except:
        print(f"error while saving the changes in the {FILE_NAME}")

def get_videos(FILE_NAME):
    try:
        with open(FILE_NAME, 'r') as file:
            videos = json.load(file)
        return videos
    except FileNotFoundError:
        return []

def main():
    FILE_NAME = "videos.json"
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
                list_all_videos(FILE_NAME)
            case "2":
                add_video(FILE_NAME)
            case "3":
                update_video(FILE_NAME)
            case "4":
                delete_video(FILE_NAME)
            case "5":
                break
            case _: # default case:
                print("Invalid option choosen, try again")

if __name__ == "__main__":
    main()