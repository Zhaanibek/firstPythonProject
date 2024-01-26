from likes import Like
from comments import Comments


class Post:
    count = 0

    def __init__(self, photo, description):
        self.photo = photo
        self.description = description
        self.likes = Like()
        self.comments = Comments()
        Post.count += 1

    def __repr__(self):
        return f"photo: {self.photo}, description: {self.description}, likes: {self.likes}, comments: {self.comments}"
