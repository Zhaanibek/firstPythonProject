class Direct:
    def __init__(self):
        self.incoming_messages = []

    def add_messages(self, message):
        self.incoming_messages.append(message)

    def __str__(self):
        return f"Direct: {self.incoming_messages}"
