from posts import Post
from user import User
import random
postslistAnton = list()


firstpost = Post(photo="1", description="Medeo")


postslistAnton.append(firstpost)
user1 = User(name="Anton", description0="19 y.o", folowers=f"{random.randint(0, 500)}",
             subscribes=f"{random.randint(0, 200)}")

firstpost.likes.add_likes()
firstpost.likes.add_likes()

firstpost.comments.add_comments("Great posts!")
firstpost.comments.add_comments("Awesome photo!")

user1.direct.add_messages("Hello!")
user1.direct.add_messages("How are you?")

print(firstpost)
print(user1)
print(user1.direct)
