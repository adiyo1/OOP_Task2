# from typing import Set
#
# from User import User
# class SocialNetwork:
#     _instance = None
#
#
#     # def __new__(cls, *args, **kwargs):
#     #     if cls._instance is None:
#     #         cls._instance = super().__new__(cls)
#     #         cls._instance._initialized = False
#     #     return cls._instance
#     #
#     # def __init__(self, name):
#     #     if self._initialized is None:
#     #         self.name = name
#     #         self.network = {}
#     #         self._users: Set[User] = set()
#     #         print(f"The social {self.name} Twitter was created!")
#     #         print("test1")
#     #         self._initialized = True
#     #     return
#     #
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             cls._instance._initialized = False
#         return cls._instance
#
#     def __init__(self, name):
#         if self._initialized:
#             return
#         self.name = name
#         self.network = {}
#         self._users: Set[User] = set()
#         print(f"The social {self.name} was created!")
#         print("test1")
#         self._initialized = True
#
#
#
#
#     def sign_up(self, username, password):
#         # Check if the user already exists
#         if username in self.network:
#             print(f"User '{username}' already exists. Please choose a different username.")
#             return None
#         if len(password) >8:
#             print(f"Password '{password}' too long.")
#             return None
#         if len(password) <4:
#             print(f"Password '{password}' too short.")
#             return None
#
#         # Create a new user and store it in the dictionary
#         new_user = User(username, password)
#         self.network[username] = new_user
#         self._users.add(new_user)
#         # print(f"User '{username}' successfully signed up.")
#         return new_user
#
#     def log_out(self,username):
#         if self._users.get(username).connect== True:
#             self._users.remove()
#             print(f"{username} disconnected")
#         else:
#             print(f"User '{username}' is already logged out")
#             return None
#
#     def log_in(self, username, password):
#         if username in self.network:
#             if password == self._users[username].password:
#                 self._users.get(username).connect= True
#                 print(f"{username} connected")
#             else:
#                 print("Incorrect password")
#
#         else:
#             print(f"User '{username}' is not exist")
#
#
from User import User

class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, name):
        if self._initialized:
            return
        self.name = name
        self.network = {}
        self._users = {}
        print(f"The social {self.name} was created!")
        print("test1")
        self._initialized = True

    def __str__(self):
        usersstr = [str(self._users[username]) for username in self._users]  # List comprehension to get user info
        return f"{self.name} social network:\n" + "\n".join(usersstr) + "\n"


    # def _new_(cls, name):
    #     if cls._instance is None:
    #         cls.instance = super().new_(cls)
    #         cls._instance.name = name
    #         cls._users = {}
    #         print(f"The social network {name} was created!")
    #     return cls._instance

    def sign_up(self, username, password):        # Check if the user already exists
        if username in self._users:
            print(f"User {username} already exists. Please choose a different username.")
            return None
        if len(password) >8:
            print(f"Password {password} too long.")
            return None
        if len(password) <4:
            print(f"Password {password} too short.")
            return None
        # Create a new user and store it in the dictionary
        new_user = User(username, password)
        self._users[username] = new_user
        print(f"User {username} successfully signed up.")
        return new_user

    def log_out(self, username):
        # if self._users.get(username).connect==True:
            self._users[username].connect=False
            print(f"{username} disconnected")
        # else:
        #     print("already logged out")

    def log_in(self, username,password):
        if password==self._users[username].password:
            self._users[username].connect = True
            print(f"{username} connected")
        # if username in self._users: