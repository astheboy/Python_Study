
# 클래스 선언

class User:
    def __init__(self, user_id, username) -> None:
        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
        print("new user being created...")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1  = User("001", "Steve")    
# user_1.id = "001"
# user_1.username = "Steve"

print(user_1.id, user_1.username)
print(user_1.followers)

user_2 = User("002", "Jacke")
# user_2.id ="002"
# user_2.username = "Jack"

print(user_2.id, user_2.username)
print(user_2.followers)


user_1.follow(user_2)  #유저 1이 유저 2를 팔로우 하기

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)