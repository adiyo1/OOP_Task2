from Post import Post, TextPost, ImagePost, SalePost
from abc import ABCMeta, abstractmethod


# User.py

# from Observers import NewPostObserver, LikeObserver, CommentObserver


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._follows = []
        self._likes = []
        self.observers= []
        self.connect= True
        self.num_posts = 0
        self.posts = []
        self.my_notification = []
        self.num_followers = 0
        # self._new_post_observer = NewPostObserver(self, self._follows)
        # self._like_observer = LikeObserver(self)
        # self._comment_observer = CommentObserver(self)


    def __str__(self):
        return (f"User name: {self.username}, Number of posts: {self.num_posts}, Number of followers: {self.num_followers}")
    def update(self, observable, notification):
        self.my_notification.append(notification)

    def notify_observer(self, notification):
        for observer in self.observers:
            observer.update(self, notification)


    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.my_notification:
            print(f"{notification}")

        # Call the function to print notifications
        # print_notifications()

    #class User:
 #   def __init__(self, username, password):
  #      self.username = username
   #     self.password = password
    #    self._follows = []

    def notify_followers(self, post):
        for follower in self._follows:
            print(f"Notification to {follower.username}: {self.username} published a {post.__class__.__name__}")

    def notify_likes(self, liker, post):
        print(f"Notification to {self.username}: {liker.username} liked your post")
    def notify_comments(self, comment, post):
        print(f"Notification to {self.username}: {comment.username}commented your post")

    def notify_newpost(self, post):
        print(f"{self.username} has a new post")


    def unfollow(self,username):
        if username in self._follows:
            self._follows.remove(username)
            username.num_followers -=1
            #self.my_notification.remove(username)
            print(f"{self.username} unfollowed {username.username}")


    def follow(self, fusername):
        newf = fusername.username
        if fusername in self._follows:
            print(f"User '{newf}' is already being followed.")
            return None

        # Create a new user and store it in the dictionary
        self._follows.append(fusername)
        fusername.num_followers +=1
        print(f"{self.username} started following {newf}")
        return None

#    def publish_post(self, post_type, content, *args):
    #def publish_post(self, post_type, prodactDes, price, location):

    def publish_post(self, post_type, content,price=None,location=None, available= True):
        self.num_posts += 1
        # def like(self, user: User):
        #     self.likes.append(user)
        #     self.notify_observers(f"{user.username} liked your post")
        #     print(f"notification to {self.name.username}: {user.username} liked your post")
        return Post.create_post(self, post_type, content, price,location, available=True)
        #if post_type == "Text":
         #   post = TextPost(content)
          #  #return TextPost(self)
           # print(self.username +" published a post:")
            #print(content)
        #elif post_type == "Image":
            #if len(args) != 1:
             #   raise ValueError("Image post requires one argument (image URL)")
            #post = ImagePost(content)
           # print()
            #print(self.username+ " posted a picture")
        #elif post_type == "Sale":
            #if len(args) != 2:
             #   raise ValueError("Sale post requires two arguments (price, location)")

            #post = SalePost(content)
        #else:
         #   raise ValueError("Invalid post type")
        #self._posts.append(post)
        #return post





