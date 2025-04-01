class User:
    # pass
    def __init__(self, user_id, user_name ):
        self.id = user_id
        self.username = user_name
        # default value
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "kalyan")
user_2 = User("002", "Eswar")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

print(user_1.username)

# user_1 = User()
# #  Creating atrributes for the class
# user_1.id = "001"
# user_1.username = "Kalyan"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Eswar"
# print(user_1.username)
# print(user_2.username)
