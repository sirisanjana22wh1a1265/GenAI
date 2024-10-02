from models.user import User
from models.video import Video

# Simulate a database
users_db = {}
videos_db = {}

def verify_user(user_id):
    if user_id in users_db:
        return {"status": "success", "user": users_db[user_id].__dict__}
    else:
        return {"status": "failure", "message": "User not found"}

def verify_video(video_id):
    if video_id in videos_db:
        return {"status": "success", "video": videos_db[video_id].__dict__}
    else:
        return {"status": "failure", "message": "Video not found"}

def add_user(user_id, name):
    users_db[user_id] = User(user_id, name)

def add_video(video_id, user_id, title):
    videos_db[video_id] = Video(video_id, user_id, title)
