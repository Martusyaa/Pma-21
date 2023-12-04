from nazarii_bryniarskyi.dict.model.User import User


class UserStack:

    def __init__(self):
        self.dictionary = {}


    def add(self, user):
        if user.username not in self.dictionary:
            self.dictionary[user.username] = user.__dict__


    def update(self, username, **args):
        if username in self.dictionary:
            self.dictionary[username].update(args)


    def remove(self, username):
        if username in self.dictionary:
            del self.dictionary[username]


    def __str__(self):
        return self.dictionary.__str__()
