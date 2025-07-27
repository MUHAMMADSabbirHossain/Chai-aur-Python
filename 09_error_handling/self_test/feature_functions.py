# custom modules
import db_operations

def add_video(videos):
    name = input("✍️  Enter new video name: ")
    time = input("✍️  Enter new video time: ")

    videos.append(
        {
            "name": name,
            "time": time
        }
    )

    db_operations.save_data(videos)

def list_all_videos(videos = []):
    print("""
**************************************************************************************************************************
""")
    
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print("""
**************************************************************************************************************************
""")

def update_video(videos):
    list_all_videos(videos)

    index = int(input("Enter video number to Update: "))

    if 1 <= index <= len(videos):
        name = input("✍️  Enter the video updated name: ")
        time = input("✍️  Enter the video updated time: ")

        videos[index - 1] = {
            "name": name,
            "time": time
        }

        db_operations.save_data(videos)
    else:
        print("❌ Invalid video index selected")

def delete_video(videos = []):
    list_all_videos(videos)

    index = int(input("Enter video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]

        db_operations.save_data(videos)
    else:
        print("❌ Invalid video index selected")