from posts import Post
from direct import Direct


class User:
    def __init__(self, name, description0, folowers, subscribes):
        self.name = name,
        self.descr0 = description0
        self.postcount = Post.count
        self.folowers = folowers
        self.subscribes = subscribes
        self.direct = Direct()

    def __str__(self):
        return (f"Username: {self.name}, description: {self.descr0}, posts: {self.postcount}, "
                f"folowers: {self.folowers}, subscribes: {self.subscribes}")

