# class Observer:
#     pass
#
# class NewPostObserver(Observer):
#     def __init__(self, user, following):
#         self.user = user
#         self.following = following
#
#     def update(self, subject):
#         if subject.author in self.following:
#             print(f"Notification to {self.user.username}: {subject.author} posted a new post: {subject.title}")
#
# class LikeObserver(Observer):
#     def __init__(self, user):
#         self.user = user
#
#     def update(self, subject):
#         if subject.author != self.user.username:
#             if subject.has_new_like():
#                 print(f"Notification to {self.user.username}: {subject.get_liker_username()} liked your post: {subject.title}")
#
# class CommentObserver(Observer):
#     def __init__(self, user):
#         self.user = user
#
#     def update(self, subject):
#         if subject.author != self.user.username:
#             if subject.has_new_comment():
#                 print(f"Notification to {self.user.username}: {subject.get_commenter_username()} commented on your post: {subject.title}")
#
#
# class User:
#     def __init__(self, username):
#         self.username = username
#
#         self._following = []
#         self._posts = []
#         self._new_post_observer = NewPostObserver(self, self._following)
#         #self._like_comment_observer = LikeCommentObserver(self)
#
#     def notify_observers(self, param):
#         pass
