class Like:
    def __init__(self, count=0):
        self.count = count

    def add_likes(self):
        self.count += 1

    def __str__(self):
        return f"{self.count}"
