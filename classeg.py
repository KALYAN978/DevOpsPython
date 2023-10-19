# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:03:50 2023

@author: kalypatn
"""

class User:

    def __int__(self, user_id, username,):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "kalyan")
user_2 = User("002", "capgemini")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)


