import random

from instagrapi import Client


account_list = []
post_list = []
comment_list = []

with open("accounts.txt", "r") as f:
    accounts = f.read().splitlines()
    for account in accounts:
        account_list.append(account)

with open("posts.txt", "r") as f:
    posts = f.read().splitlines()
    for post in posts:
        post_list.append(post)

with open("comments.txt", "r") as f:
    comments = f.read().splitlines()
    for comment in comments:
        comment_list.append(comment)


class Bot:
    def login(self, account):
        self.cl = Client()
        self.username, self.password = account.split(":")
        self.cl.login(self.username, self.password)
        self.user_id = self.cl.user_id

    def comment(self, post, comment):
        print(post)
        print(comment)


for account in account_list:
    bot = Bot()
    bot.login(account)
    for post in post_list:
        comment = random.choice(comment_list)
        bot.comment(post, comment)