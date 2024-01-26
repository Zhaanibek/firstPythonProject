class Comments:
    def __init__(self):
        self.comments = []

    def add_comments(self, text):
        self.comments.append(text)

    def __str__(self):
        return f"{self.comments}"
