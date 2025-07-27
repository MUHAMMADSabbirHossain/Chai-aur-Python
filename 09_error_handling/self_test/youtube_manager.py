# custom modules
import feature_functions
import db_operations

def main():
    print("✅ Youtube Manager software is running...")

    videos = db_operations.load_data()

    while True:
        print("""
        Youtube Manager | choose an option 
        0. Exit
        1. List all youtube videos
        2. Add a youtube video
        3. Update a youtube video details
        4. Delete a youtube video
        """)

        choosen_option = input("✍️  Enter your choice: ")

        match choosen_option:
            case "0":
                # print("Exit")
                return
            case "1":
                feature_functions.list_all_videos(videos)
            case "2":
                feature_functions.add_video(videos)
            case "3":
                feature_functions.update_video(videos)
            case "4":
                feature_functions.delete_video(videos)
            case _:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()

print("✅ Youtube Manager software is closed...")
