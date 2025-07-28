from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient("mongodb+srv://practice-crud:mEmLNSfkE7mUF4Ci@cluster0.kq2asyp.mongodb.net/ytmanager")
client = MongoClient("mongodb+srv://chai_aur_python:chai_aur_python@cluster0.kq2asyp.mongodb.net/", tlsAllowInvalidCertificates=True)
# Not a good idea to include id and password in code files
# tlsAllowInvalidCertificates=True - Not a good way to handle ssl
print(client)
# print(client.list_database_names())

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one(
        {
            "name": name,
            "time": time
        }
    )

def list_videos():
    for vidoe in video_collection.find():
        print(f"ID: {vidoe['_id']}, Name: {vidoe['name']} and Time: {vidoe['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {
            '_id': ObjectId(video_id)
        },
        {
            '$set': {
                'name': new_name,
                'time': new_time
            }
        }
    )

def delete_video(video_id):
    video_collection.delete_one(
        {
            '_id': ObjectId(video_id)
        }
    )
    # TODO: ✅debug this video_id problem

def main():
    while True:
        print("\n Youtube Manager")
        print("1. List all youtube videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")

            add_video(name, time)
        elif choice == "3":
            list_videos()

            video_id = input("Enter video ID to update: ")  
            name = input("Enter video updated name: ")
            time = input("Enter video updated time: ")

            update_video(video_id, name, time)
        elif choice == "4":
            list_videos()

            video_id = input("Enter video ID to delete: ")

            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()